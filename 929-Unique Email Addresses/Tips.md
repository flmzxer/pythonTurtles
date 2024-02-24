1.  Create datastructure for storing unique values
2.  While iterating throught list of e-mails:
    -  Split e-mails into local name and a domain name
    -  Split local name by "+" rule
    -  Replace "." with nothing
    -  Combine local name and a domain name back and store resulting e-mails in our datastructure
3.  Return lengh of our datastructure to get the number of different addresses that actually receive mails.



### 1. Create datastructure for storing unique values
<details><summary>Tip</summary>use set()</details>

### 2. While iterating throught list of e-mails:
<details><summary>Tip</summary>for e in emails:</details>

#### Split e-mails into local name and a domain name
<details><summary>Tip</summary>localName, domainName = e.split("@")</details>

#### Split local name by "+" rule
<details><summary>Tip</summary>localName = localName.split("+")[0]</details>

#### Replace "." with nothing
<details><summary>Tip</summary>localName = localName.replace(".","")</details>

#### Combine local name and a domain name back and store resulting e-mails in our datastructure
<details><summary>Tip</summary>uniqueEmailsSet.add((localName, domainName))</details>

### 3. Return lengh of our datastructure to get the number of different addresses that actually receive mails.           
<details><summary>Tip</summary>return len(uniqueEmailsSet)</details>
