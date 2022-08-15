print('''
                          .-=-.
                         /  ! )\
                      __ \__/__/
                     / _<( ^.^ )
                    / /   \ c /O
                    \ \_.-./=\.-._     _
                     `-._  `~`    `-,./_<
                         `\' \'\`'----'
                       *   \  . \          *
                            `-~~~\   .
                       .      `-._`-._   *
                             *    `~~~-,      *
                   ()                   * )
                  <^^>             *     (   .
                 .-""-.                    )
      .---.    ."-....-"-._     _...---''`/. '
     ( (`\ \ .'            ``-''    _.-"'`
      \ \ \ : :.                 .-'
       `\`.\: `:.             _.'
       (  .'`.`            _.'
        ``    `-..______.-'
                  ):.  (
                ."-....-".
          jgs .':.        `.
              "-..______..-"
''')
print("Welcome to Genii Wish.")
print(
    "You have the opportunity to get your wish awarded by the Genii. Choose wisely !"
)

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

genii_way = input(
    "Hello lucky person, choose 1 way I can help you. Type Love or Money or Career\n"
)

choice = genii_way.lower()

if choice == "love":
    love = input(
        "The choice of the heart ! Please name the person you desire:\n")
    love_name = love.lower()
    print(
        f"Congratulations {love_name} and you will become a beautiful couple and will live happily ever after ! Goodbye !"
    )

if choice == "money":
    money = int(
        input(
            "Financial security, I understand ! Please give me the amount you desire: Enter a number between 0 and 999999\n"
        ))
    print(
        f"Congratulations, tomorrow you will find ${money} in you bank account ! Goodbye !"
    )

if choice == "career":
    career = input(
        "Professional growth, exciting choice ! Enter 'new job' or 'promotion'\n"
    )

    career_choice = career.lower()

    if career_choice == "new job":
        print(
            "Congratulations, in 1 month you will start a new job with double your current salary ! Goodbye !"
        )
    elif career_choice == "promotion":
        print(
            "Congratulations, in 1 month you will be promoted to a more senior role with double your current salary ! Goodbye !"
        )
