class Profile:
    def __init__(self, name, mobile, password):
        self.name = name   #  public
        self._mobile = mobile   # protected
        self.__password = password    #private

    def show_mobile(self):
        print(self._mobile)



profile1 = Profile("Derbes", "87477777777")

print(profile1.name)
profile1.name = "Askar"
print(profile1.name)
# print(profile1.mobile)
profile1.show_mobile()



