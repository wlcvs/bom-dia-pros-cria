from get_contacts import get_contacts
from it_s_7_am import it_s_7_am
from get_image import get_image
from index_random import index_random
from send_image import send_image
from delete_image import delete_image

def main():
    while True:
        get_contacts()
        if it_s_7_am:
            get_image(index_random)
            send_image()
            delete_image()

if __name__ == '__main__':
    main()