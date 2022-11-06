import os
from os.path import exists
from sys import exit
obfuscationTypes = ['Strong', 'Medium', 'Weak']
for x in range(1, 3):
    print()
print('   ________  ________  ________  ________  ________  ________  ________  ________  ________  ________ ')
print('  ╱        ╲╱        ╲╱        ╲╱        ╲╱        ╲╱        ╲╱    ╱   ╲╱        ╲╱    ╱   ╲╱        ╲')
print(' ╱         ╱         ╱         ╱         ╱       __╱        _╱         ╱       __╱         ╱        _╱')
print('╱       __╱        _╱         ╱         ╱       __╱╱       ╱╱         ╱       __╱         ╱--       ╱ ')
print('╲______╱  ╲____╱___╱╲________╱╲__╱__╱__╱╲________╱ ╲______╱ ╲___╱____╱╲________╱╲________╱╲________╱  ')
print('Prometheus Obfuscator                                                           Automated in Python')
print('discord.gg/c2f4qwSynp')
print('By ninjaninja140')
for x in range(1, 3):
    print()
correctDir = os.path.exists(os.getcwd()+'\scripts')
if correctDir:
    print(':: Prometheus :: Hey there! \n:: Prometheus :: Welcome to Prometheus, before we start please make sure that your script is placed in scripts and you know what its called.')
    for x in range(1, 3):
        print()
    filename = input(
        ':: Obfuscator :: What file are you obfuscating? (File must end in .lua) ')
    if filename.endswith('.lua'):
        file_exists = os.path.exists(os.getcwd()+'/scripts/'+filename)
        filepath = os.getcwd()+'/scripts/'+filename
        print(':: Prometheus :: Searching for file...')
        print(':: Obfuscator :: Searching in ', filepath)
        if file_exists == True:
            print()
            print(':: Prometheus :: Found file!')
            print()
            print(
                ':: Obfuscator :: Obfuscation levels: Strong (Larger File - Could Error), Medium, Weak (Smaller File)')
            obfuscationLevel = input(
                ':: Obfuscator :: What level of obfuscation are you going to run at? ')
            if obfuscationLevel == 'Strong':
                print(':: Prometheus :: Please note that strong obfuscation is dangerous and may not work, please confirm you want to continue.')
                yn = input(
                    'Please confirm (Type YES to continue, type NO to exit.): ')
                if yn == 'YES':
                    print('Continuing...')
                    print()
                    print(':: Prometheus :: Obfuscating!')
                    print(
                        ':: Prometheus :: Running '+"prometheus.exe --preset Strong "+filepath)
                    print(':: Obfuscator :: Preset Selected: Strong')
                    os.popen(
                        "prometheus.exe --preset Strong "+filepath)
                    print()
                    print(':: Obfuscator :: Obfuscated file!')
                    input(':: Prometheus :: Press Enter to Exit.')
            elif obfuscationLevel == 'Medium':
                print()
                print(':: Prometheus :: Obfuscating!')
                print(
                    ':: Prometheus :: Running '+"prometheus.exe --preset Medium "+filepath)
                print(':: Obfuscator :: Preset Selected: Medium')
                os.popen(
                    "prometheus.exe --preset Medium "+filepath)
                print()
                print(':: Obfuscator :: Obfuscated file!')
                input(':: Prometheus :: Press Enter to Exit.')
            elif obfuscationLevel == 'Weak':
                print()
                print(':: Prometheus :: Obfuscating!')
                print(
                    ':: Prometheus :: Running '+"prometheus.exe --preset Weak "+filepath)
                print(':: Obfuscator :: Preset Selected: Weak')
                os.popen(
                    "prometheus.exe --preset Weak "+filepath)
                print()
                print(':: Obfuscator :: Obfuscated file!')
                input(':: Prometheus :: Press Enter to Exit.')
        else:
            print()
            print(':: Prometheus :: This is not a valid file!')
            input(':: Prometheus :: Press Enter to Exit.')
    else:
        print()
        print(':: Prometheus :: Your file MUST be a .lua file!')
        input(':: Prometheus :: Press Enter to Exit.')
else:
    print()
    print(':: Prometheus :: Prometheus cannot be ran in the incorrect dir.')
    input(':: Prometheus :: Press Enter to Exit.')
