import requests
import os

hashmasks_dir = "hashmasks_highres"
starting_index = 10141
ending_index = 16384


# Make new directory for hashmasks.
if not os.path.exists(hashmasks_dir):
    os.mkdir(hashmasks_dir)

# Pull the hashmasks.
for pre_release_index in range(ending_index):
    # Convert from the pre-release index to the post-release index.
    post_release_index = (ending_index - starting_index + pre_release_index) % ending_index

    print(f"Pulling hashmask ID #{post_release_index}...")
    # Pull the image from online.
    img_data = requests.get(f"https://hashmasksstore.blob.core.windows.net/hashmasks/{pre_release_index}.jpg").content
    # Write the image to file.
    with open(f"{hashmasks_dir}/{post_release_index}.jpg", 'wb') as mask_file:
        mask_file.write(img_data)
