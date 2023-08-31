import requests
import re
from bs4 import BeautifulSoup
import time
from colorama import Fore


def usernameurl():

    global usernamess
    response = requests.get(furl)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the meta tag with the specified name attribute
    meta_tag = soup.find("meta", {"name": "twitter:title"})

    if meta_tag:
        content_value = meta_tag.get("content", "")
        
        # Extract the username from the content value
        username = content_value.split("(")[-1].split(")")[0].replace("@", "")
        print(Fore.BLUE +username)
        print(username,file=f)
        usernamess += 1 
    else:
        
        print(Fore.LIGHTRED_EX +bizname)
        print(bizname,file=u)

def get_first_google_result_url(query):    
    global found
    found = 0

    base_url = "https://www.google.com/search"
    params = {
        "q": query,
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    
    response = requests.get(base_url, params=params, headers=headers)
     
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        search_results = soup.find_all("div", class_="tF2Cxc")
        
        if search_results:
            first_result = search_results[0]
            link = first_result.a.get("href")
            found = 1 
            return link
        else:
            return "No search results found."
    else:
        print("IP BANNED GOTTA WAIT 24H.") 
    






print(Fore.GREEN + r"""\                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
               ...''....                                              
              .:lodoool:,.                                            
             .lddl,,cddddl,.                                          
            .;ddo,..:doccodl,.                                        
            .:ddl' .cdl'.'codl,.                                      
            .lddc. 'ldc.  .':odl;.              ........              
           .:ddo,. ,od:.    ..:odl;'.        ..;cooooooc;.            
       .',;looc,. .;dd;.      ..:oddl;.   .';coddddl,,lddc.           
       'loddl,.   .:do,         ..:codo;,;lodl:,:od:..;ddo,           
       ...;ldl;.  .cdl'           ..,odddol:'. .;dd;..;ddo'           
          .,odo,. 'ldc.        ..,:loddl;'.    .:do,..:ddl.           
           'odd:..,od:.     ..,:odool;'.       .cdl' .:ddl.           
           ,odd;..;dd;.  ..,coddo:'..          .ldc.  'ldo;.          
          .,odo, .:do,..,codolodo:...          ,od:.  ..:lol;'.       
           ,odo;..cdoccodo:,...;ldol:'.       .;od;.  .':lool:.       
           .:odoccodddl:,..     .,lodoc'.     .:do,  .cddl,...        
            ..,;::::;'.           .',cdoc'.   .cdl' .:ddl'            
                                     .,cdoc'. .ldl. 'ldd:.            
                                       .,codc,;odc..,odd;.            
                                         .'codddd:..cddl'             
                                           .':oddoclddo,.             
                                             ..';;::;,..              
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
""")
















output_file = input(Fore.YELLOW +"enter output txt file (WITHOUT .txt) : ") 
print("")

while True:
    file_input = input(Fore.YELLOW + 'Enter business names txt file (WITHOUT .txt) : ') + '.txt'

    with open(file_input, 'r') as fcheck:
        li = fcheck.readlines()
        lines = [line for line in li if line.strip() != ""]
        total_line = len(lines)      
        if total_line > 100:
            print(Fore.RED + 'ERROR: TXT FILE LINES > 100')
        else:
            print("")
            print(Fore.GREEN + 'Total lines in the file:', total_line)
            print("")
            print(Fore.CYAN + "Here are Found Usernames : ")
            print("")
            break  



usernamess = 0
unfound = 0

with open (output_file + "_unfound"+ ".txt" , "w") as u:
    with open(output_file + ".txt", "w") as f:
        with open(file_input, 'r') as file:
            
            for line in file:
                if line.strip() == "":
                    pass

                else:
                    unfound += 1 
                    bizname = line.strip()
                    query = 'site:instagram.com + "@" + '
                    query_url = query + '"' + bizname + '"'
                    furl = get_first_google_result_url(query_url)
                    #print("First Google search result URL:", furl)
                    
                    if found == 1 :
                        if "/p/" in furl:
                            usernameurl()
                        elif "/tv/" in furl:
                            usernameurl()
                        elif "/reel/" in furl:
                            usernameurl()
                        elif "/explore/" in furl :
                            pass
                        
                        else:
                            username_patterns = [
                                r"https?://(?:www\.)?instagram\.com/([^/?]+)(?:[/?]|$)"
                            ]

                            username = None

                            # Iterate through patterns to find a match
                            for pattern in username_patterns:
                                match = re.search(pattern, furl)
                                if match:
                                    username = match.group(1)
                                    break

                            if username:
                                print(Fore.BLUE +username)
                                print(username,file=f)
                                usernamess += 1 
                    
 
print('')
time.sleep(1)
print(Fore.GREEN + 'Usernames founded : ',usernamess , ' out of ' ,total_line)
print('')
time.sleep(1)
print(Fore.GREEN +'Exported To ---->>> ', output_file)
print(Fore.CYAN+'')
print(Fore.CYAN + 'See you later L9wada')
time.sleep(2)



