# UPPER LEVEL API
import auto_dict
import auto_syn
import re
from mxproxy import mx
Cache=mx.Cache

class Page:
	'''docstring'''
	def __init__(self,string):
		self.string=self.remove_comments(string)
		self.soup=mx.make_soup(self.string)
		self.cleaned=''
		self.bsoup=''
		self.hardwords=''

	def remove_comments(self,string):
		return re.sub(r'<!.*?->','', string) 

	def preserve_only_href_src(self):
		for x in self.soup.findAll():
			if x.name not in ['a','img']:
				del x.attrs
		return self

	def remove_empty(self,bsoup):
		for x in bsoup.findAll():
			if not x.text:
				print(x.text)
				x.decompose()
		return bsoup

	def get_hardwords(self,string,threshold=6):
		result=set(re.findall(r'[\w]*',string))
		result={x for x in result if len(x)>=threshold }
		return result
		
if __name__ == '__main__':
	body='''"<span class=\"hs_cos_wrapper hs_cos_wrapper_meta_field hs_cos_wrapper_type_rich_text\" data-hs-cos-general-type=\"meta_field\" data-hs-cos-type=\"rich_text\" id=\"hs_cos_wrapper_post_body\" style=\"\"><p>Here's the good news: marketing and ad agencies are getting serious about hiring new talent.</p><br><p>According to data from the\u00a0Bureau of Labor Statistics, advertising, promotions, and marketing manager\u00a0employment is <a href=\"https://www.bls.gov/ooh/management/advertising-promotions-and-marketing-managers.htm#tab-6\" target=\"_blank\">expected to rise 9%\u00a0by 2024</a> -- which is faster than the average for all occupations.\u00a0</p><br><!--more--><br><p>The not-so-good\u00a0news? The competition is fierce.<!--HubSpot Call-to-Action Code --><span class=\"hs-cta-wrapper\" id=\"hs-cta-wrapper-4ec95757-585e-40cf-9189-6b3885074e98\"><span class=\"hs-cta-node hs-cta-4ec95757-585e-40cf-9189-6b3885074e98\" id=\"hs-cta-4ec95757-585e-40cf-9189-6b3885074e98\"><!--[if lte IE 8]><div id=\"hs-cta-ie-element\"></div><![endif]--><a href=\"https://cta-redirect.hubspot.com/cta/redirect/53/4ec95757-585e-40cf-9189-6b3885074e98\" target=\"_blank\"></a></span></span><!-- end HubSpot Call-to-Action Code --></p><br><p><span style=\"letter-spacing: 0px; background-color: transparent;\">If you want to stand out in a crowded applicant pool, you need to make sure your resume is free from filler phrases,\u00a0</span><span style=\"letter-spacing: 0px; background-color: transparent;\">clich\u00e9s, and\u00a0things that make you sound unprofessional or unprepared. To help you out, we've compiled a list of 10 vague, overused, and downright boring phrases you should cut from your resume.</span></p><br><p><span>Are you guilty of using any of these on your resume?</span></p><br><h2><span>10 Phrases You Should Cut from Your Resume</span></h2><br><h3>1) \"I was responsible for ...\"</h3><br><p>The things you were responsible for at your last job don't actually say anything about your performance. For example, I was once \"responsible\" for watering a plant, but that plant is now dead.</p><br><p>Instead of presenting your experience like a checklist of completed tasks, focus on your accomplishments. What did you do at your last job that made a big impact? What did you particularly excel at? Agencies want to see what you achieved, not just what your day-to-day looked like.</p><br><h3>2) \"I have experience in ... \"</h3><br><p>Saying you \"have experience\" doing\u00a0something is passive and vague, and can almost always be replaced by a more active word. Instead of saying you \"have experience\" working with a particular strategy, dig into the specifics of what you've accomplished, e.g.: \"I A/B tested\u00a0email nurturing campaigns to develop a workflow that converted prospects at 35%.\"</p><br><p>See? That sounds much better than, \"I have experience with email nurturing campaigns.\"</p><br><h3 id=\"last\">3) \"I assisted with ... \"</h3><br><p>Saying you assisted with something doesn't explain <em>how</em> exactly you contributed. Instead of saying you \"assisted\" with a project, get specific, and don't be afraid to own your accomplishments.</p><br><p>Even if you only worked on a small section of a successful project, explain how your contributions fit into the final product, e.g.: \"Optimized landing pages as part of a global nurturing campaign.\"</p><br><h3>4) \"I'm proficient in Microsoft Word, Excel, and PowerPoint.\"</h3><br><p>This phrase usually gets tacked onto the end of resumes in the \"skills\" section, but you're probably better off\u00a0cutting it out entirely.\u00a0</p><br><p>Unless you're applying for a job\u00a0that specifically asks for advanced experience with Microsoft Office, there's really no need to mention this. These days, it's pretty much a given that you have some level of proficiency with Microsoft Office. Including it as one of your skills not only comes across as outdated, it can also make it seem like you don't have any more relevant\u00a0skills worth mentioning.\u00a0</p><br><h3>5) \"I ran social media.\"</h3><br><p>\"Social media\" often gets thrown around on resumes without specifics -- which can make you sound like you don't really know what you're talking about.</p><br><p>Social media isn't a skill or a discipline, it's a tool that can be leveraged to accomplish business goals. Saying you \"ran social media\" or \"worked in social media\" is like saying you ran PowerPoint. What did you <em>do</em> with social media? How did you use it to accomplish a real business goal?\u00a0</p><br><h3>6) \"I have strong communication / writing skills.\"</h3><br><p>Do you remember in middle school writing class when the teacher introduced the concept of <em>show, don't tell</em>? That still applies today.\u00a0</p><br><p><em>Show</em> hiring managers you have strong writing and communication skills by creating a stellar resume and cover letter -- and triple check for spelling and grammar.\u00a0Mistakes happen to the best of us, but they're easy to weed out of an important job application.</p><br><h3>7) \"I'm a motivated self-starter.\"</h3><br><p>If you're an adult who can't\u00a0get yourself motivated to be productive and work hard, then you probably shouldn't be applying for\u00a0a\u00a0demanding marketing\u00a0job. Leave out this overused phrase, and instead highlight a time you went above and beyond on a project.\u00a0</p><br><h3>8) \"I'm goal-oriented / results-oriented.\"</h3><br><p>Here's a fact: nobody hates accomplishing goals. If you want to prove you're particularly driven, give concrete\u00a0examples of goals you've met -- or better yet, goals you've beaten.\u00a0</p><br><h3>9) \"I'm a\u00a0marketing\u00a0ninja / rock star.\"</h3><br><p>Giving yourself a quirky title\u00a0might seem like a cute, creative way to stand out in a sea of \"digital marketing managers,\" but it can come across as more than a little obnoxious.</p><br><p>Even if the hiring manager doesn't\u00a0personally mind the unconventional headline, it doesn't actually explain what you do. Don't take the risk: Describe yourself in a straightforward, professional way.\u00a0</p><br><h3>10) \"Disruptive / ground-breaking\"</h3><br><p>Marketers tend to love big, bold adjectives, but hyperbolic copy doesn't belong on your resume. Cut the clich\u00e9d descriptions and keep things direct and sincere.\u00a0</p><br><p><em>What phrases do you think people should stop using in their resumes? Let us know in the comments.</em></p><br><p><em><!--HubSpot Call-to-Action Code --><span class=\"hs-cta-wrapper\" id=\"hs-cta-wrapper-77221356-781b-4250-bd96-53d9ec6c3a99\"><span class=\"hs-cta-node hs-cta-77221356-781b-4250-bd96-53d9ec6c3a99\" id=\"hs-cta-77221356-781b-4250-bd96-53d9ec6c3a99\"><!--[if lte IE 8]><div id=\"hs-cta-ie-element\"></div><![endif]--><a href=\"https://cta-redirect.hubspot.com/cta/redirect/53/77221356-781b-4250-bd96-53d9ec6c3a99\" target=\"_blank\"></a></span></span><!-- end HubSpot Call-to-Action Code --></em></p><br><div id=\"slidebox\"><a class=\"close\">\u00a0</a><!--HubSpot Call-to-Action Code --><span class=\"hs-cta-wrapper\" id=\"hs-cta-wrapper-9b7f1c12-479a-45cb-9f9e-d104e0bd66be\"><span class=\"hs-cta-node hs-cta-9b7f1c12-479a-45cb-9f9e-d104e0bd66be\" id=\"hs-cta-9b7f1c12-479a-45cb-9f9e-d104e0bd66be\"><!--[if lte IE 8]><div id=\"hs-cta-ie-element\"></div><![endif]--><a href=\"https://cta-redirect.hubspot.com/cta/redirect/53/9b7f1c12-479a-45cb-9f9e-d104e0bd66be\" target=\"_blank\"></a></span><br><br><br></span><!-- end HubSpot Call-to-Action Code --></div></span>" '''
	myPage=Page(body)
	print(myPage.string)
	# body=remove_comments(body)
	# bsoup=mx.make_soup(body)
	# remove_attributes(bsoup)
	# remove_empty(bsoup)
	# print(bsoup)