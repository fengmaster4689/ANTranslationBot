# ANTranslationBot
Bot for Discord with various features and incorporates various devop tools

Features:
1. automatically translate japanese to english and vice versa
	- calls chatgpt api or google translate api
2. setup selected computers as servers if they are active, and if they aren't use the AWS cloud
	- will likely lightsail server? need to figure out why and document it
3. an automatic tenor gif message based on tag
	- for example, !hug will send a hug themed gif
4. add a way to send a pronounciation recording for a selected translation
	- start with using google translate for simple a cheap method
	- Later, we can implement azure's text to speech for better prounounciation. Both should be an option since azure's translation will cost more money.
5. Automatic text to speech translator between the 2 languages
design:
- start with drafting a design for which tools to use with the reasoning and how it should theoretically connect with the other tools to make the feature work
- coded in python
	- we could use a linux VM too?
- each feature should be a separate file
- version controlled in github
- simple unit tests for code
- each commit should run CI/CD
	- build, run, test, doxygen/sphinx
	- should run in a ubuntu docker container
- runs in AWS cloud
	- AWS controlled by terraform
	
-how to include ansible?
	- perhaps have the aws cloud to be the main server and push configurations to our local machines?