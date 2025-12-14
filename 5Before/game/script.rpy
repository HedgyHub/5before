# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define J = Character("Jack")

define L= Character("Lily")
define B=Character("Chłopiec")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    # Scene 1: Jack arrives at the apartment. Meets Lily, her boyfriend and mysterious little boy.

    J "Mogła przekazać dziewczynki Lily."

    "Myślę stojąc przed naszym zapyziałym dwupiętrowcem. Płatki śniegu opadają powoli na moje włosy, przypominając mi, że znowu wybiegając rano z domu nie zabrałem czapki."
    
    "W końcu się rozchoruję i umilę kolegom z pracy dzień niekończącą się arią smarkania i kaszlu."

    J "Nie mogę tu tak stać. Pewnie są głodne, a robi się już późno."

    "Wahając się ledwie chwilę wzdycham i otwieram drzwi, po czym wchodzę na klatkę schodową. Wspinając się powoli, stopień po stopniu, mijam ściany,które rozpaczliwie domagają się renowacji."

    "Odpadająca farba to najmniejszy problem. Jakiś niedoszły Picasso od siedmiu boleści wymalował sprayem symbol. Niekończąca się plątaniną linii i kropek, które pewnie miały być w zamierzeniu podpisem."

    "Wiesz, taki pospolity bazgroł, które te niedorozwoje zostawią na każdej, wystarczająco długo niepilnowanej, powierzchni."
    
    "Muszę o tym pogadać z tym gościem spod trójki. Kurwa, czy my w ogóle mamy fundusz remontowy? Rachunki za wynajem tej rudery są już wystarczająco wysokie."

    "Z zamyślenia wyrywa mnie głos dochodzący z drugiego piętra. Piętro na którym mieszkam. Niedaleko dwunastki zauważam Lily pochylająca się nad małym chłopcem." 
    
    L "Odwiedzasz kogoś z tego bloku? Zgubiłeś się?"
    
    "Dzisiaj jej włosy zawinięte są w 2 grube warkocze, opadające symetrycznie z dwóch stron twarzy. "

    "Czemu moje myśli powędrowały od razu do jej włosów? Może to te..."

    B "..."

    "Dżwięk moich butów uderzających o posadzkę sprawia, że oboje zwracają swoje twarze w moją stronę"

    "Twarz chłopca nie wyraża żadnych emocji. Jego wyraziste piwne oczy obserwują mnie uważnie gdy podchodzę do nich. Przywołuję na twarz lekki uśmiech. Rozmowa z Lily"

    L "Dobry wieczór panie Jack."

    J "Dobry, dobry Lily. Co to za chłopak?"

    "Lily przekręca głowę zdezorientowana."

    L "On chyba..."

    "Chłopak wpada jej w słowo."

    B "Przepraszam"



    # This ends the game.

    return
