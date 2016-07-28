#!/usr/bin/perl

use strict;
use warnings;
use Net::SSH::Expect;
my $ip = "";
my $user = "";
my $pass = "";
    my $ssh = Net::SSH::Expect->new(
        host => $ip ,
        user => $user,
        password => $pass,
        ssh_option  => "-o UserKnownHostsFile=/dev/null",
    );

    eval
    {
        my $output = $ssh->login();
        die "$output";
    };

        if ($@)
    {
        my $err = $@;
        if ($err !~ m/Blue Coat/i)
        {
            #SysLog::Print("error", "Couldn't ssh to SG : $err \n");
            print "Couldn't ssh to SG : $err \n"
            #return undef;
        }

    }
    $ssh->close();

# for((i=1;i<250;i++)); do nohup perl login.pl & done
