print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'

''')
print("Willkommen zur Schatzsuche.")
print("Deine Mission ist es, den Schatz zu finden.")
wahl1 = input('Du stehst an einer Kreuzung, wohin möchtest du gehen? Tippe "links" oder "rechts"\n').lower()

if wahl1 == "links":
    wahl2 = input('Du bist an einen See gekommen. In der Mitte des Sees befindet sich eine Insel. '
                  'Tippe "warten", um auf ein Boot zu warten, oder tippe "schwimmen", um über den See zu schwimmen.\n').lower()

    if wahl2 == "warten":
        wahl3 = input("Du bist unversehrt auf der Insel angekommen. "
                      "Dort ist ein Haus mit 3 Türen. Eine rote, eine gelbe und eine blaue. "
                      "Welche Farbe wählst du?\n").lower()

        if wahl3 == "gelb":
            print("Du hast den Schatz gefunden! GEWONNEN!")
        elif wahl3 == "blau":
            print("Du bist in ein Loch mit Haien gefallen. SPIEL VORBEI!")
        elif wahl3 == "rot":
            print("Du bist in die Feuergrube gefallen. SPIEL VORBEI!")

    else:
        print("Du wurdest von einem Hai gefressen. SPIEL VORBEI!")
else:
    print("Du bist in ein Loch gefallen. SPIEL VORBEI!")