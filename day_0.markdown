#Day 0 

###The aim: Follow the instructions from [the invitation letter](https://groups.google.com/forum/#!topic/omooc/HLuK4TKDYC8)
---
####Issues 

* GitBook

	Q: Coulnd't integrate the GitHub repository with GitBook one. 
	
	A: Edit the Permission level of GitHub account on acount settings: [https://www.gitbook.com/@username/settings]
![alt text](https://github.com/yzha3917/omooc.py/blob/master/pics/gitbook.jpg?raw=true)


	Q: how to adjust structure of book. 
	
	A: SUMMARY.md is the file. It links the local files to the table of contents. It's vital to learn that the path should be relative path, i.e. /book/chapter_1/section_1.md
	

	
===
* Markdown

	Q<sup>1</sup>: Couldn't insert pictures in Markdown file. 

		1. local pics stored in the same directory as the MD file can be referred in a relative path: [/pics/pic.jpg]
		2. push pics into GitHub/dropbox to acquire a URL: [https://github.com/yzha3917/omooc.py/blob/master/pics/gitbook.jpg]
		3. If the image is still failed to render, [?raw=true] should be append to the url/relative path. 


	Q: Need to resize the pic. 
	
	A<sup>2</sup>: For Mou editor, instead of appending [?raw=true], [ =100x100] could be uesd for resizing. 100 means 100 pixels, and the first number is for width, the 2nd one is for height.
	
	
	
	Q: Need to add footnotes on MD, and it must be compatible with GitHub Flavoured MD.
	
	A<sup>3</sup>: It doesn't. Altough it is visually acceptable to use superscript tags to fake one. Just add 	
	```[<sup>#</sup>] ```, # is the number of footnotes,and then writing down footnotes in the end with [===] as seperation. 
	
===	
	
	
* Git

	Q: How to discard the uncommited changes. 
	
	A: ```git checkout file.name```
	
===


[1]: [Markdown to insert and display an image on GitHub repo](http://webapps.stackexchange.com/questions/29602/markdown-to-insert-and-display-an-image-on-github-repo)

[2]: [how to change image size markdown](http://stackoverflow.com/questions/14675913/how-to-change-image-size-markdown)

[3]: [How do I add footnotes to GitHub flavoured Markdown?](http://stackoverflow.com/questions/25579868/how-do-i-add-footnotes-to-github-flavoured-markdown)
