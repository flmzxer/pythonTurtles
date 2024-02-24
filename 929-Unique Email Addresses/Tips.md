1.  Create datastructure for storing unique values
2.  While iterating throught list of e-mails:
    -  Split e-mails into local name and a domain name
    -  Split local name by "+" rule
    -  Replace "." with nothing
    -  Combine local name and a domain name back and store resulting e-mails in our datastructure
3.  Return lengh of our datastructure to get the number of different addresses that actually receive mails.
