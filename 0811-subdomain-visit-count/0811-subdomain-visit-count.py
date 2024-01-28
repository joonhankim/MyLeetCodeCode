class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_map = defaultdict(int)
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            domains = domain.split('.')
            for i in range(len(domains)):
                subdomain = '.'.join(domains[i:]) 
                domain_map[subdomain] += count
        return ['{} {}'.format(count, domain) for domain, count in domain_map.items()]

                