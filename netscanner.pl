#!/usr/bin/perl


local $logdir  = "/root/netlogs";
foreach $dir (qw(by-ip by-mac by-alias)) {
    if (! -d "$logdir/$dir") { system("mkdir -p $logdir/$dir") }
}


local %alias = ();
local $aliasFile   = "/root/lib/netscanner.cfg";
local @aliasOutput = `cat $aliasFile`;
chomp @aliasOutput;
@aliasOutput = grep(!/^\s*$/,@aliasOutput);
@aliasOutput = grep(!/^\s#/, @aliasOutput);
foreach $line (@aliasOutput) {
    local ($mac,$alias) = ((split('\s+',$line))[0,1]);
    if ( ($mac) and ($alias) ) {
        $alias{$mac} = $alias;
    }
}


sub scan {
    local @output = `nmap -n -sP 192.168.0.1/24`;
    chomp @output;
    @output = grep(!/^\s*$/,@output);
    @output = grep(!/^Starting Nmap/,@output);
    @output = grep(!/^Nmap done/,@output);
    return @output;
}


local $date   = `date`; chomp($date);
local @output = scan();
local $ip     = '';
local $mac    = '';


foreach $line (@output) {
    if ( $line =~ m/^Nmap scan/ ) {
        $ip =  $line;
        $ip =~ s/Nmap scan report for //;
    }
    if ( $line =~ m/^MAC Address/ ) {
        $mac =  $line;
        $mac =  (split('\s+',$mac))[2];
    }
    if ( $line =~ m/^MAC Address/ ) {
        local $alias = $alias{"$mac"};
        if ( $alias eq "" ) { $alias = "unknown" };
        $logstring = "$date  $ip  $mac  $alias";
        if ($ip)    { system("echo $logstring >> $logdir/by-ip/$ip"      ) }
        if ($mac)   { system("echo $logstring >> $logdir/by-mac/$mac"    ) }
        if ($alias) { system("echo $logstring >> $logdir/by-alias/$alias") }


        $ip    = "";
        $mac   = "";
        $alias = "";
    }
}
