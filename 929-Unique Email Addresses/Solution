class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmailsSet = set()

        for e in emails:
                localName, domainName = e.split("@")
                localName = localName.split("+")[0]
                localName = localName.replace(".","")
                uniqueEmailsSet.add((localName, domainName))
        return len(uniqueEmailsSet)
