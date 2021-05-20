
import webbrowser, sys, pyperclip

# webbrowser.open('https://automatetheboringstuff.com') - opens a web browser with the url
if len(sys.argv) > 1:
    address = '+'.join(sys.argv[1:])
    print(address)
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/{0}'.format(address,))