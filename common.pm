package common ;
use Exporter 'import';
@EXPORT_OK = qw(getDate getTime epocToDateTime trim_ws_left trim_ws_right trim_ws_lr truncate_string unique_array digit2
                digitn basename dirname roundup msleep padzero intendHost max min sendMail readFile writeFile appendFile
                archivename);
# FILE          common.pm
# VERSION       2.01
# PURPOSE       Suite of general purpose functions.
# AUTHOR        Peter Rhodes.
# DATE          04/06/2014
#
# RELEASE HISTORY  #####################################################################################################
########################################################################################################################
#### Date          Version     Contributor      Comment
#### 18/09/2014    2.03        Peter Rhodes     Added readFile and writeFile.
#### 11/09/2014    2.02        Peter Rhodes     Fixed msleep name error.
#### 20/06/2014    2.01        Peter Rhodes     Add function intendHost().
#### 04/06/2014    2.01        Peter Rhodes     Add function roundup().
####                                            Add function padzero(), and replaced 'digit2' within time functions.
#### 30/05/2014    2.0         Peter Rhodes     Extensive Re-write to make it suitable for general-purpose.
####   /  /2012    1.0         Peter Rhodes     Original Implementation.
########################################################################################################################
########################################################################################################################
#
#        1         2         3         4         5         6         7         8         9         0         1         2
#23456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
#
########################################################################################################################
# PART 1 DATETIME FUNCTIONS.
#        getDate             Get the current Date - Format yyyy/mm/dd .
#        getTime             Get the current Time - Format hh:mm:ss .
#        epocToDateTime      Return Date and Time in "yyyy/mm/dd" and "hh:mm:ss" for a given epoc value.
# PART 2 STRING MANIPULATION FUNCTIONS.
#        trim_ws_left        Remove whitespace from beginning of string.
#        trim_ws_right       Remove whitespace from end of string.
#        trim_ws_lr          Remove whitespace from beginning and end of string.
#        truncate_string     Elegantly truncate string to a given length.
#        unique_array        De-duplicate list.
#        digit2              Return a string with at least two digits.
#        digitn              Return a number with at least n digints.
#        basename            Return the basename.
#        dirname             Return the dirname.
# PART 3 NUMERIC FUNCTIONS.
#        roundup             Round a number up.
# PART 4 UNCLASSIFIED.
#        msleep              Sleep that allows sub-second granularity. e.g. msleep(0.322) - 322 milliseconds.
#        padzero             Pad out numbers with zeros for formatting purposes.
#        intendHost          A Helper Function to ensure that host characteristics are correct before proceeding.
#        max
#        min
#        sendMail
#        readFile
#        writeFile
#        listequality
#        archivefilename
#        debuglist


########################################################################################################################
# PART 1 DATETIME FUNCTIONS.
########################################################################################################################

################################################################################
### str = getDate()
### Get the current Date - Format yyyy/mm/dd
################################################################################
sub getDate {
    local  ($second,$minute,$hour,$dayOfMonth,$month,
            $yearOffset,$dayOfWeek,$dayOfYear,$daylightSavings) = localtime();
    local  $year  = 1900 + $yearOffset;
    local  $month = $month + 1;

    ($month,$dayOfMonth)=padzero(2,$month,$dayOfMonth);
    local  $date = "$year/$month/$dayOfMonth";

    return $date;
}
################################################################################

################################################################################
### str = getTime()
### Get the current Time - Format hh:mm:ss
################################################################################
sub getTime {
    local  ($second,$minute,$hour,$dayOfMonth,$month,
            $yearOffset,$dayOfWeek,$dayOfYear,$daylightSavings) = localtime();

    ($hour,$minute,$second)=padzero(2,$hour,$minute,$second);
    local  $time = "$hour:$minute:$second";

    return $time;
}
################################################################################

################################################################################
### str,str = epocToDateTime(int)
### Return Date and Time in "yyyy/mm/dd" and "hh:mm:ss" for a given epoc value
################################################################################
sub epocToDateTime {
        local $epoc = shift;
        local ($sec,$min,$hour,$day,$month,$year) = localtime($epoc);
        $year      += 1900;
        $month     += 1;
        return ( "$year/".digit2($month)."/".digit2($day)
                ,digit2($hour).":".digit2($min).":".digit2($sec) );
}
################################################################################


########################################################################################################################
# PART 2 STRING MANIPULATION FUNCTIONS.
########################################################################################################################

################################################################################
### str = trim_ws_left(str)
### Remove whitespace from beginning of string.
################################################################################
sub trim_ws_left {
    local  $string  =  shift;
           $string  =~ s/^\s+//;
    return $string;
}
################################################################################

################################################################################
### str = trim_ws_right(str)
### Remove whitespace from end of string.
################################################################################
sub trim_ws_right {
    local  $string  =  shift;
           $string  =~ s/\s+$//;
    return $string;
}
################################################################################

################################################################################
### str = trim_ws_lr(str)
### Remove whitespace from beginning and end of string.
################################################################################
sub trim_ws_lr {
    local  $string = shift;
           $string = trim_ws_left ($string);
           $string = trim_ws_right($string);
    return $string;
}
################################################################################

################################################################################
### str = truncate_string(str)
### Elegantly truncate string to a given length by using the sequence "..."
### to signify that the string is longer than the given length.
################################################################################
sub truncate_string {
    local $string        = shift;
    local $field_length  = shift;

    local $target_length = $field_length-1;
    local $string_length = length($string);

    if ( $string_length > $target_length ) {
          $string  = substr($string,0,($target_length-3));
          $string .= "...";
    }

    $string = sprintf("%-${field_length}s",$string);
    $string =~ s/\s+$//;

    return $string;
}
################################################################################

################################################################################
### list = unique_array(list)
### Return @list without duplicates.
################################################################################
sub unique_array {
        local  @array = @_;
        local  %seen  = ();
        local  @unique = grep { ! $seen{$_} ++ } @array;
        return @unique;
}
################################################################################

################################################################################
### str = digit2(str)
### Place a leading 0 onto a single digit number.
### e.g. "7" -> "07"
################################################################################
sub digit2 {
        return substr("0$_[0]",-2) if length($_[0]) == 1 || ( return $_[0]) ;
}
################################################################################

################################################################################
### str = digitn(str,num)
### Return a number padded with zeros at the front.
###
################################################################################
sub digitn {
        local $number    = shift;
        local $targetlen = shift;

        while (length($number) < $targetlen) {
            $number = "0$number";
        }
return $number;
}
################################################################################

################################################################################
### str = basename(str)
### Return the basename of a path e.g.
### "/var/sadm/install/contents" --> "contents"
### "/usr/bin/pagesize"          --> "pagesize"
################################################################################
sub basename {
    local  $path     = shift;
    local  $basename = (split("/",($path)))[-1];
    return $basename;
}
################################################################################

################################################################################
### str = dirname(str)
### Return the dirname of a path e.g.
### "/var/sadm/install/contents" --> "/var/sadm/install"
### "/usr/bin/pagesize"          --> "/usr/bin"
################################################################################
sub dirname {
    local  $path    =  shift;
    local  $dirname =  $path;
           $dirname =~ s!/?[^/]*/*$!!;
    return $dirname;
}
################################################################################



########################################################################################################################
# PART 3 NUMERIC FUNCTIONS.
########################################################################################################################

################################################################################
### int = roundup(int)
### Round a number upwards to 0 decimal places.
################################################################################
sub roundup {
    local $n = shift;
    return(($n == int($n)) ? $n : int($n + 1))
}
################################################################################



########################################################################################################################
# PART 4 UNCLASSIFIED.
########################################################################################################################

################################################################################
### msleep(int)
### Sleep that allows sub-second granularity. e.g. msleep(0.322);
################################################################################
sub msleep {
    local $time = shift;
    select(undef,undef,undef,$time);
}

################################################################################
### list = padzero(str,list)
### Pad out numbers with trailing zeros if necessary.
###  first argument is the number of digits.
###  second argument is a list of numbers to be "padded" - list can contain single element.
###  If the first argument is "max" or a number less than zero, then the padding is set to
###  the value of the longest element within the list.
################################################################################
sub padzero {
    local $padding             = shift;
    local @numberList          = @_;
    local ($number,$numberMax) = ();

    if ($padding == "max") {$padding = 0};
    if ($padding le 0) {
        foreach $number (@numberList) {
            if (length($number) gt $padding) { $padding = length($number) };
        }
    }

    @numberList=map { sprintf("%0${padding}d",$_) } @numberList;
    return @numberList;
}
################################################################################


################################################################################
### $ = getUname()
### return uname - helper function for intendHost
### even though "$^O" returns the OS type - we don't use it because it returns
### ... the OS for which the Perl Binary was built. Which may not be the same!
################################################################################
sub getUname {
    local @unamePath = qw(/usr/bin /bin);
    local $uname     = "";
    foreach $path ( @unamePath ) {
        if ( -e "$path/uname"  ) {
            $uname  = "$path/uname";
            last;
        }
    }
    return "$uname";
}
################################################################################


################################################################################
### $ = intendHost($,$)
### Return success only if the selected host attribute  matches the input argument.
###  ...  we leave it up to the calling logic to call exit.
###  ...  remember to use ^ and $ to enforce strict matching.
###  e.g  (intendHost("os","^SunOS$")) or exit;
################################################################################
sub intendHost {
    local  $type      = "$ARGV[0]";
    local  $regex     = "$ARGV[1]";
    local  $uname     = getUname();
    local  $typeflag  = "";

    ( $type eq "os"       ) and $typeflag = "s";
    ( $type eq "platform" ) and $typeflag = "i";
    ( $type eq "isa"      ) and $typeflag = "p";
    ( $type eq "release"  ) and $typeflag = "r";
    ( $typeflag eq ""     ) and return;

    local  $machine   = `$uname -$typeflag`;
    chomp  $machine;
    local  $test      = ( $machine =~ m/$regex/ );
    return $test;
}
################################################################################


################################################################################
### $ = max(@)
################################################################################
sub max {
    splice(@_, ($_[0] > $_[1]) ? 1 : 0, 1);
    return ($#_ == 0) ? $_[0] : max(@_);
}
################################################################################

################################################################################
### $ = min(@)
################################################################################
sub min {
    splice(@_, ($_[0] > $_[1]) ? 0 : 1, 1);
    return ($#_ == 0) ? $_[0] : min(@_);
}
################################################################################

################################################################################
### $ = sendMail(@)
################################################################################
sub sendMail {
    local ($to,$from,$subject,@message) = @_;
    my $sendmail = '/usr/lib/sendmail';
    open(MAIL, "|$sendmail -oi -t");
    print MAIL "From: $from\n";
    print MAIL "To: $to\n";
    print MAIL "Subject: $subject\n\n";
    foreach $line (@message) { print MAIL "$line\n" };
    close(MAIL);
}
################################################################################

################################################################################
### @ = readFile($)
################################################################################
sub readFile {
    local $file=shift;
    open my $handle,'<',"$file";
    chomp(my @lines = <$handle>);
    close $handle;
    return @lines;
}
################################################################################

################################################################################
### _ = writeFile($,@)
################################################################################
sub writeFile {
    local $file=shift;
    @lines = @_;
    open my $handle,'>',"$file";
    foreach my $line (@lines) {
        print $handle "$line\n";
    }
    close $handle;
}
################################################################################

################################################################################
### _ = appendFile($,@)
################################################################################
sub appendFile {
    local $file=shift;
    @lines = @_;
    open my $handle,'>>',"$file";
    foreach my $line (@lines) {
        print $handle "$line\n";
    }
    close $handle;
}
################################################################################

################################################################################
### $test = listequality (\@list1,\@list2,\@list3,...)
################################################################################
sub listequality {
    local @reflist = @_;

    local $listcount = (@_);                             # Number of lists.
    local @itemcount = map {                             # Item count for each list.
        local $ref = $_;
        local $count=(@{$ref});
        $count;
    } @reflist;

    local $max      = common::max(@itemcount);           # Largest number of items.
    local $equality = 1;
    local $content,$content0;

    for $item_counter (0 .. ($max-1)) {                  # Iterate through list items.
        for $list_counter (0 .. ($listcount-1)) {        # Iterate through lists.
            $content  = @{$reflist[$list_counter]}[$item_counter];
            if ($list_counter == 0) {
                $content0 = $content;
                print "P0>$content0<\n";
            } else {
                if ($content ne $content0) {$equality = 0}
print ">$content0<>$content<>$equality<\n";
            }
        }
    }
    return $equality;
}
################################################################################

################################################################################
###
################################################################################
sub archivename {
    local $file    = shift;
    local $arglist = shift;

    local $base       = basename($file);
    local $path       = dirname ($file);
    local $processPID = $$;

    local ($second,$minute,$hour,$day,$month,
           $yearOffset,$dayOfWeek,$dayOfYear,$daylightSavings) = localtime();
    $yearOffset  += 1900;
    $month        = digit2($month);
    $day          = digit2($day);
    $hour         = digit2($hour);
    $minute       = digit2($minute);
    $second       = digit2($second);

    local $dateStamp = "${yearOffset}${month}${day}";
    local $timeStamp = "${hour}${minute}${second}";
    local $pidStamp  = "${processPID}";
    local $stamp     = "";
    local $dot       = "";

    @arglist = split('[,\s]+',$arglist);
    foreach $arg (@arglist) {
        if ( $arg =~ m/dot/  ) { $dot    = '.'           }
        if ( $arg =~ m/pid/  ) { $stamp .= "-$pidStamp"  }
        if ( $arg =~ m/date/ ) { $stamp .= "-$dateStamp" }
        if ( $arg =~ m/time/ ) { $stamp .= "-$timeStamp" }
    }
    local $archive = "${path}/${dot}${base}${stamp}";
    return $archive;

}


################################################################################
###
################################################################################
sub debuglist {
    local @arglist = @_;
    foreach (@arglist) {print ">$_<\n"}
}
