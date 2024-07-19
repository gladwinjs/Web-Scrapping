import instaloader

# Create an instance of Instaloader
bot = instaloader.Instaloader()

# Prompt user for Instagram credentials
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")

try:
    # Login with the provided credentials
    bot.login(username, password)
except instaloader.TwoFactorAuthRequiredException as e:
    # If 2FA is required
    print("Two-factor authentication required.")
    
    # Prompt for the 2FA code
    two_factor_code = input("Enter the 2FA code: ")
    
    try:
        # Complete the 2FA process
        bot.two_factor_login(two_factor_code)
        print("2FA authentication successful")
    except instaloader.BadCredentialsException:
        print("Incorrect 2FA code or other login error")
    except instaloader.TwoFactorAuthRequiredException as e:
        print("Invalid 2FA code. Please try again.")
    except Exception as e:
        print(e)
except instaloader.BadCredentialsException:
    print("Incorrect login credentials")
except Exception as e:
    print(e)

# Now load the profile using the username
try:
    profile = instaloader.Profile.from_username(bot.context, username)
    print(f"Profile loaded successfully: {profile.username}")
except instaloader.ProfileNotExistsException as e:
    print(f"Profile {username} does not exist.")
except Exception as e:
    print(e)

# Print the type of profile object
print(type(profile))

print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography, profile.external_url)

# Retrieve the usernames of all followers
followers = [follower.username for follower in profile.get_followers()]

# Retrieve the usernames of all followees
followees = [followee.username for followee in profile.get_followees()]

# Print profile details
print(followers)

# Retrieve and print likes and comments on posts
print("\nFetching posts...")
for post in profile.get_posts():
    print(f"Post URL: {post.url}")
    print(f"Likes: {post.likes}")
    print(f"Comments: {post.comments}")
    print("----")
