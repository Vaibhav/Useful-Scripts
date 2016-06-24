import os
import datetime


print "Please choose what type of file you are searching for:"
print "For image files, type i"
print "For video files, type v"
print "For audio files, type a"
print "To search for a specified file extension, Enter any other key"
choice = raw_input()

if choice == "i" or choice == "a" or choice == "v":
    iva(choice);
else:
    custom(choice);


def iva(choice):
    start = datetime.datetime.utcnow()
	print("Start: " + str(start))


	start_loc = os.path.abspath(os.sep)

	img_list = ['.tif', '.tiff', '.jpg', '.jpeg', '.gif', '.png', '.jif',
                '.jfif', '.jp2', '.jpx', '.j2k', '.j2c', '.fpx', '.pcd', '.bmp']

    vid_list = ['.mp4', '.avi', '.arf', '.264', '.dav', '.mov', '.mkv', '.avc', '.dv4',
                '.trec', '.dvr', '.exo', '.swf', '.yify', '.asf', '.qt', '.h264', '.h260',
                '.flv', '.swf', '.mpeg', '.mpg', '.wmv', '.divx', '.xvid']

	aud_list = ['.mp3', '.wma', '.aiff', '.m4a', '.m4p', '.mpa', '.wav', '.ra', '.rm',
                '.ram', '.mid', '.ogg', '.flac', '.aac']

	if choice == "i":
    	ext_list = img_list
	elif choice == "v":
    	ext_list = vid_list
	elif choice == "a":
    	ext_list = aud_list

	extensions = tuple(ext_list)

	result = open('results.csv', 'w')

	try:
	for dirName, subdirList, files in os.walk(start_loc):
    	for fname in files:
    		if fname.endswith(extensions):
    			full_path = os.path.join(dirName, fname)
				result.write("{0}\n".format(full_path))

	finally:
		result.close()

		endtime = datetime.datetime.utcnow()
		print("End: " + str(endtime))

		total = endtime - start
		print("Total: " + str(total / 60))
