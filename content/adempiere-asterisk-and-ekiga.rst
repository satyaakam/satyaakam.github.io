Adempiere , Asterisk and Ekiga
##############################
:date: 2009-06-08 13:56
:author: satya
:category: Adempiere, Ekiga, Sip
:tags: Sip, Voip
:slug: adempiere-asterisk-and-ekiga
:status: published

`Michael Judd <http://www.mikejudd.com/>`__ setup an asterisk system for
`adempiere <http://www.adempiere.org>`__ community to use. once the
accounts for people are created you can access it using a voip softphone
or a hard phone.

With the service we can currently conference, and call extensions for
free. Mike have the servers located in data centre in London which has
plenty of bandwidth. (1,000GB/month) he has some inbound UK numbers
which can be routed through different call groups and queues. You can
schedule timezones and only route to certain extensions at certain times
of the day (so as not to wake you up at night).

Currently, there is no outbound calling (as that costs money), but he
can add additional telephone numbers for different countries and route
them directly to you.

People who want to join the system will be able to call and transfer
calls to each other - so this could be used as a collaboration tool for
support.

Mike is presently looking for other interested parties to try this out -
please contact michael dot judd at akunagroup dot com if you are
interested.

I have tested it using `Ekiga <http://www.ekiga.org>`__ on 256 Kbps
bandwidth from Airtel Broadband services , it works well some screen
shots below

[gallery]

account settings i have done in Ekiga

| service:
|  username:
|  password: (same for voicemail)

| You can try the following numbers:
|  102 - Mike Judd
|  304 - Satyag
|  # - Directory
|  \*43 - echo test
|  \*60 - speaking clock
|  411 - Directory dial by name
|  \*97 - voicemail

You can try other sip clients from this `Sip
software <http://en.wikipedia.org/wiki/List_of_SIP_software#SIP_clients>`__
list and report to mike how things are working at your end
