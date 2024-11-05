"""object oriented programming"""


class Profile:  # each instance of Profile will have variables: declaring attributes
    username: str
    bio: str
    followers: list[str]
    # followers: int
    following: int
    private: bool

    def __init__(self):  # initializing attributes with default values
        self.username = "usr1"
        self.bio = ""
        self.followers = []
        # self.followers = 0
        self.following = 0
        self.private = False


my_prof: Profile = Profile()
my_prof.username = "comp110fan"
my_prof.followers.append("unclatinos")
print(my_prof.followers)


class Profiler:
    username: str
    followers: list[str]
    following: list[str]

    def __init__(self, usr):
        self.username = usr
        self.followers = []
        self.following = []

    # Method definitions
    def follow(self, username: str) -> None:
        self.following.append(username)

    def get_following(self) -> list[str]:
        return self.following


my_prof: Profiler = Profiler("comp110fan")
print(my_prof.following)
my_prof.follow("unc.latinosintech")
print(my_prof.following)


class Coordinate:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_dist(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx


p0: Coordinate = Coordinate(10.0, 0.0)
p0.translate_x(-5.0)
print(p0.get_dist())
