import subprocess as sp

from ..core.read import *
from ..core.create import *
from ..core.delete import *


def add_menu(connection, cursor):
    while True:
        _ = sp.call("clear", shell=True)
        print("==============ADD MENU==================")
        print("0. Back\n1. Actor\n2. Director\n3. Brand\n4. Channel\n5. Show\n6. Product\n7. Ad\n8. Gaurdian\n")
        ch = input("Enter your choice > ")
        if ch == '0':
            return
        elif ch == '1':
            addActor(connection, cursor)
        elif ch == '2':
            addDirector(connection, cursor)
        elif ch == '3':
            addBrand(connection, cursor)
        elif ch == '4':
            addChannel(connection, cursor)
        elif ch == '5':
            addShow(connection, cursor)
        elif ch == '7':
            addProduction(connection, cursor)
        elif ch == '8':
            addGaurdian(connection, cursor)
        else:
            print("Invalid option\n")
        connection.rollback()
        _ = input("Enter a key to continue")


def delete_menu(connection, cursor):
    while True:
        _ = sp.call("clear", shell=True)
        print("==============DELETE MENU==================")
        print("0. Back\n1. Actor\n2. Director\n3. Brand\n4. Channel\n5. Show\n6. Product\n7. Ad\n8. Guardian\n9. Remove Ad from Show\n10. Remove Brand from Actor's preferred brands\n")
        ch = input("Enter your choice > ")
        if ch == '0':
            return
        elif ch == '1' or ch == '2':
            deletePerson(connection, cursor)
        elif ch == '3':
            deleteBrand(connection, cursor)
        elif ch == '4':
            deleteChannel(connection, cursor)
        elif ch == '5':
            deleteShow(connection, cursor)
        elif ch == '6':
            deleteProduct(connection, cursor)
        elif ch == '7':
            deleteAd(connection, cursor)
        elif ch == '8':
            deleteGuardian(connection, cursor)
        elif ch == '9':
            deleteDisplayed(connection, cursor)
        elif ch == '10':
            deletePrefers(connection, cursor)
        else:
            print("Invalid option\n")

        _ = input("Enter a key to continue")


def read_menu(connection, cursor):
    while True:
        _ = sp.call("clear", shell=True)
        print("==============READ MENU==================")
        print("0. Back\n1. Get all Actors\n2. Get all Directors\n3. Get all Brands\n4. Get all Channels\n5. Get all Shows\n6. Get all Products\n7. Get all Ads\n8. Get Ad-Show Relations\n9. Get Actor's preferred brands\n10. Get all Guardians\n11. Actors with Physical features\n12. Average ad production cost\n13. Maximum preferred brands\n14. Partial text search for show\n15. Get best shows for an ad\n16. Partial text search for actor\n17. Shows with surcharge less than a value\n18. Maximum of sum of the contract money of brand\n19. Bill for Ad\n20. Shows list by amount\n")
        ch = input("Enter your choice > ")
        if ch == '0':
            return
        elif ch == '1':
            readActors(connection, cursor)
        elif ch == '2':
            readDirectors(connection, cursor)
        elif ch == '3':
            readBrands(connection, cursor)
        elif ch == '4':
            readChannels(connection, cursor)
        elif ch == '5':
            readShows(connection, cursor)
        elif ch == '6':
            readProducts(connection, cursor)
        elif ch == '7':
            readAds(connection, cursor)
        elif ch == '8':
            getAdShows(connection, cursor)
        elif ch == '9':
            getActorBrands(connection, cursor)
        elif ch == '10':
            getGuardians(connection, cursor)
        elif ch == '11':
            actorsByFeatures(connection, cursor)
        elif ch == '12':
            avgProduction(connection, cursor)
        elif ch == '13':
            maxPreferred(connection, cursor)
        elif ch == '14':
            searchShow(connection, cursor)
        elif ch == '15':
            showsForAd(connection, cursor)
        elif ch == '16':
            searchActor(connection, cursor)
        elif ch == '17':
            surchargeLessThan(connection, cursor)
        elif ch == '18':
            maxProdCost(connection, cursor)
        elif ch == '19':
            adBill(connection, cursor)
        elif ch == '20':
            showList(connection, cursor)
        else:
            print("Invalid option\n")

        _ = input("Enter a key to continue")
