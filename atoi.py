class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # convert a string to an integer
        
        # return 0 if no conversion ccould be returned
        ret = 0

        # check for over/underflow  (how???)
        int_max=2147483647
        int_min=-2147483648

        negative=False
        record=False
        print "***** str=",str
        for i in range (len(str)):
            print "checking i=",i,"stri=",str[i]
            if (str[i]==" ") :
                #discard leading whitespace but stop if we've hit trailing whitespace
                if (record==True):
                    break
            elif ((str[i]=="+") or (str[i]=='-')):
                # check for leading + or - (if none assume +)
                #  peek: next char must be a digit
                if (i==len(str)-1):
                    return 0
                elif ((str[i+1] < '0') or (str[i+1] > '9')):
                    return 0
                if (str[i]=="-"):
                    negative=True
            elif ((str[i]>='0') and (str[i]<='9')):
                digit = ord(str[i]) - ord('0')
                ret=ret*10+digit
                record=True
            else :
                break

        if (negative==True):
            ret=0-ret

        if (ret>int_max):
            return int_max
        if (ret<int_min):
            return int_min

        return ret


sol = Solution()
s="Hello   -893 foo"
a = sol.myAtoi(s);
print "s=",s," a=",a


s="Hello"
a = sol.myAtoi(s);
print "s=",s," a=",a

s="09182374109238471209384712098472918734918734918237"
a = sol.myAtoi(s);
print "s=",s," a=",a


s="+-2"
a = sol.myAtoi(s);
print "s=",s," a=",a

s="-0012a42"
a = sol.myAtoi(s);
print "s=",s," a=",a

s="- 321"
a = sol.myAtoi(s);
print "s=",s," a=",a

s=" b11228552307"
a = sol.myAtoi(s);
print "s=",s," a=",a


s="   010"
a = sol.myAtoi(s);
print "s=",s," a=",a
