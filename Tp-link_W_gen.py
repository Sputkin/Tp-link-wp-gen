#-*- coding:utf-8 -*-

"""
 * Copyright (c) 2015 Sputkin .
 * 
 * Tp-link_W_gen is free software: you can redistribute it and/or modify  
 * it under the terms of the GNU General Public License as published by  
 * the Free Software Foundation, version 3.
 *
 * Tp-link_W_gen is distributed in the hope that it will be useful, but 
 * WITHOUT ANY WARRANTY; without even the implied warranty of 
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License 
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from itertools import product
import sys

def main():
    print ""
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"      
    print "!       Respect the privacy of others."
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print ""
    counter = 0
    wordlist = open("wordlist.txt","w")
    combinations = product("0123456789",repeat=8)
    print ("[+] The file will be saved in the current directory !!")
    print ("[+] create wordlist...")
    for list in combinations:
        wordlist.write("".join(list)+"\n") 
        counter +=1
                 
    return counter
 
if __name__ == "__main__":
        size = main()
        print("[+] total key generated %s size %d Mb"%(size,(size*9)/1000000))
