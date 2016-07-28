#!/usr/bin/perl

BEGIN { $ENV{PERL_LWP_SSL_VERIFY_HOSTNAME} = 0 }

# turn on perl's safety features

use strict;
use warnings;



# create a new browser
use WWW::Mechanize;
use IO::Socket::SSL;
use Data::Dumper;


my $mech = WWW::Mechanize->new(ssl_opts => {

    SSL_verify_mode => IO::Socket::SSL::SSL_VERIFY_NONE,

    verify_hostname => 0, # this key is likely going to be removed in future LWP >6.04

});


$mech->agent_alias( 'Linux Mozilla' );
$mech->max_redirect(0);

$mech->credentials( "user1" ,"1resu");
$mech->proxy(['http'] , 'http://10.168.100.146:8080');



# browser will open the auth debug page

my $url = "http://sg-146.qa-auth11.waterloo.bluecoat.com";
$mech->get("http://www.example.com");
my $cookie_jar = $mech->cookie_jar; # returns a HTTP::Cookies object
$cookie_jar->scan(sub { print Dumper \@_ });

print Dumper($cookie_jar);
&separate;

print "\n\n\n headers:\n";
$mech->dump_headers();
&separate;


print "\n\n\n response:\n";
print Dumper($mech->response());
&separate;

#print "\n\n\n post:\n";
#print $mech->post();

#FOR DEBUGGING
print "\n\n\n links:\n";
$mech->dump_links();
print "\n\n\n text:\n";
$mech->dump_text();
print "\n\n\n forms:\n";
$mech->dump_forms();


sub separate
{
print"####################################################################################\n";
              return 1;
}
