# Canvas-Bot

Canvas-Bot is a web scraper for the Canvas LMS designed for alt media professionals. It extracts all media content from a given course page as well as all media content from directly linked third party websites that may be important for a particular course. 

To scrape a Canvas LMS Course.


````
# Create a CanvasBot object with the course ID.
Bot = CanvasBot("330")
Bot.start()

# all_content_to_json will return the location of the saved JSON file. 
content = Bot.Content.all_content_to_json()
````



An example JSON output of all the instructional content found in a Canvas Course: https://sfsu.box.com/s/rphude4tjily6jba7x8flt6kpeaa9fzd


An example content tree of a Canvas LMS page produced by the scraper. 
````
<Canvas Course Root ID: 330>
├── <Announcements https://sfsu.instructure.com/courses/330/announcements - Success>
│   └── <Announcement-0-Announcements>
│       └── <Discussion https://sfsu.instructure.com/courses/330/discussion_topics/1311 - Success>
├── <Assignments https://sfsu.instructure.com/courses/330/assignments - Success>
├── <Home https://sfsu.instructure.com/courses/330/pages/homepage - Failed>
├── <Modules https://sfsu.instructure.com/courses/330/modules - Success>
│   ├── <Module-0-WelcomeModule>
│   ├── <Module-1-Welcome!>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14349 - Success>
│   │   │   └── ( ContentURLVideo - https://sfsu.zoom.us/j/82573895498?pwd=RGdqQmZnU1djNjVDK2RxczJGZ1pkZz09 - None - 1 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14350 - Success>
│   │   │   └── <ExternalPage https://open.spotify.com/playlist/6iPTtDiQOFAPyKliouJNcT?si=e4a1241149c64a22 - Success>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14352 - Success>
│   │   │   └── <ExternalPage https://jamboard.google.com/d/1rOwXS0O7zoWw3Vbo3u1z62_-oKBCvfUITzkA_Ynk5CI/viewer?f=0 - Success>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14354 - Success>
│   │   │   └── <ExternalPage https://join.slack.com/t/metrofacultyl-jvu5468/shared_invite/zt-udryn8ea-Y9SKahpfgCyaxRIiSF3LJw - Success>
│   │   │       └── ( ContentURLVideo - https://www.youtube.com/channel/UCY3YECgeBcLCzIrFLP4gblw - None - 1 )
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/community-builders - Success>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38744/ - Human Bingo.doc )>
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/percent-c2-percent-a0-our-schedule-percent-c2-percent-a0tuesday-percent-2c-august-16thwednesday-percent-2c-august-17th-percent-c2-percent-a0thu - Success>
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/welcome-percent-21 - Success>
│   │   │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38704/ - celestebyers_justicefirst.jpg )>
│   │   │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38722/ - Screen Shot 2020-08-03 at 12.40.30 PM.png )>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38740/ - Savi 1.jpg )>
│   │   └── ( ContentImage - /images/icons/mc-assignment-pub.svg ALT:TRUE)
│   ├── <Module-2-Day1-Monday--August16th,2021>
│   │   ├── <Discussion https://sfsu.instructure.com/courses/330/discussion_topics/1312 - Success>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14357 - Success>
│   │   │   ├── ( ContentURLVideo - //www.youtube.com/embed/aLF2mQMABoQ - None - 2 )
│   │   │   └── ( ContentURLVideo - https://www.youtube.com/watch?v=aLF2mQMABoQ&feature=youtu.be - None - 2 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14358 - Success>
│   │   │   └── <ExternalPage https://metro.sfsu.edu/about-metro-academies - Success>
│   │   │       ├── ( ContentImage - https://www.sfsu.edu/images/SFState_logo_color.jpg ALT:TRUE)
│   │   │       └── ( ContentURLVideo - https://www.youtube.com/user/metroacademies - None - 2 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14359 - Success>
│   │   │   └── <ExternalPage http://www.ccsf.edu/en/educational-programs/learning-community/StudentResources/metro-transfer-academy.html - Success>
│   │   │       ├── ( ContentImage - /sites/default/files/styles/400_with/public/2020/inline-media/metro-office%20%281%29.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - /themes/custom/ccsf/assets/images/logo.png ALT:TRUE)
│   │   │       └── ( ContentURLVideo - https://www.youtube.com/embed/aLF2mQMABoQ?autoplay=0&start=0&rel=0 - None - 2 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14360 - Success>
│   │   │   ├── ( ContentURLVideo - //www.youtube.com/embed/eKuPfKELIUM - None - 2 )
│   │   │   └── ( ContentURLVideo - https://www.youtube.com/watch?v=eKuPfKELIUM&feature=youtu. - None - 2 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14363 - Success>
│   │   │   └── <ExternalPage https://www.npr.org/sections/codeswitch/2019/03/21/704930088/the-student-strike-that-changed-higher-ed-forever - Success>
│   │   │       ├── ( ContentImage - https://media.npr.org/assets/img/2018/08/03/npr_theindicatorpm_podcasttile_sq-2b1d594a6a7d6c70618924796b4ffd778e9d33a8.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/assets/img/2019/02/26/we_otherentitiestemplatesat_sq-cbde87a2fa31b01047441e6f34d2769b0287bcd4-s100-c85.png ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/assets/img/2019/02/26/we_otherentitiestemplatesun_sq-4a03b35e7e5adfa446aec374523a578d54dc9bf5-s100-c85.png ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/assets/img/2019/03/21/ap_690121020_custom-c0907ef26022cfe98302e3262febdc4e65b44083-s1100-c50.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/assets/img/2019/03/21/ap_690121020_custom-c0907ef26022cfe98302e3262febdc4e65b44083-s1200.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/assets/img/2019/03/21/smeraji-sfsualum1_slide-0da600761a479ca7168d851c30e284bdd5a68071-s1100-c50.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/assets/img/2019/03/21/smeraji-sfsualum1_slide-0da600761a479ca7168d851c30e284bdd5a68071-s1200.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/assets/img/2019/03/21/smeraji-sfsualum2_slide-6d31fd7c2df72c98201dcee1162985ea14e54524-s1100-c50.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/assets/img/2019/03/21/smeraji-sfsualum2_slide-6d31fd7c2df72c98201dcee1162985ea14e54524-s1200.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/assets/img/2019/09/19/shortwave-tile_final2_sq-266c8cc0cd2cb3e6213b36cbd0009cbd3331a990.png ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/assets/img/2020/03/24/undefined_sq-63f9f4b46bb9031d67f9785b66818f4befbab8bc-s800-c15.jpg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://media.npr.org/assets/img/2020/09/21/codeswitch_shereenmarisolmeraji_2020_2_sq-decc5e15d6cb93f8a955385f8175de25cd94f52c-s100-c85.jpg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://media.npr.org/assets/img/2021/03/22/pchh_podcast-tile-21_sq-16ede85b6991ee201c4a839ece7e5bcc19da55ef.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/assets/img/2022/03/01/stateofukraine_podcast-tile_sq-00f5186913b3ff3b6d8e7ad01ae19ada5e4682b5.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/branding/sections/codeswitch/branding_main-e50ee2a2b6c9cc5b43ae0d52c496620dfdcacf74.png ALT:TRUE)
│   │   │       ├── ( ContentImage - https://media.npr.org/chrome/programs/logos/all-things-considered.png ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/chrome/programs/logos/fresh-air.png ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/chrome/programs/logos/morning-edition.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/chrome/programs/logos/up-first.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://media.npr.org/chrome_svg/music-logo-dark.svg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://media.npr.org/chrome_svg/music-logo-light.svg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://media.npr.org/chrome_svg/npr-logo.svg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://media.npr.org/documents/about/people/bios/biophotos/kbates_2006_sq-27577360673bae30495cc8730c73060437b87c51-s100-c85.jpg ALT:TRUE)
│   │   │       ├── ( ContentURLAudio - https://podcasts.apple.com/podcast/1112190608?mt=2&at=11l79Y&ct=nprdirectory - None - 2 )
│   │   │       ├── ( ContentURLAudio - https://www.npr.org/podcasts/510282/pop-culture-happy-hour - None - 2 )
│   │   │       ├── ( ContentURLAudio - https://www.npr.org/podcasts/510325/the-indicator-from-planet-money - None - 2 )
│   │   │       ├── ( ContentURLAudio - https://www.npr.org/podcasts/510351/short-wave - None - 2 )
│   │   │       └── ( ContentURLAudio - https://www.npr.org/podcasts/510366/state-of-ukraine - None - 2 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14364 - Success>
│   │   │   ├── ( ContentURLVideo - //www.youtube.com/embed/SKNGDXILmiA - None - 2 )
│   │   │   └── ( ContentURLVideo - https://www.youtube.com/watch?v=SKNGDXILmiA - None - 2 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14369 - Success>
│   │   │   └── <ExternalPage https://docs.google.com/forms/d/1SRiFRyrD_XDL9LaBVl8O6lSZsgXAM6yPE1mT_0LqEqc/edit - Success>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14370 - Success>
│   │   │   └── <ExternalPage https://sfsu.co1.qualtrics.com/jfe/form/SV_cuohTuNRFrzsLwF - Success>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14374 - Success>
│   │   │   └── <ExternalPage https://docs.google.com/forms/d/1Ay73J9R0rmGTosyJ77ALfcUGQxndIHseJZnjrDswJ48/edit - Success>
│   │   │       └── ( ContentImage - https://www.gstatic.com/images/branding/googlelogo/svg/googlelogo_dark_clr_74x24px.svg ALT:TRUE)
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14377 - Success>
│   │   │   ├── ( ContentURLVideo - //www.youtube.com/embed/_URPOzlTADE - None - 2 )
│   │   │   └── ( ContentURLVideo - https://www.youtube.com/watch?v=_URPOzlTADE - None - 2 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14380 - Success>
│   │   │   └── <ExternalPage https://medium.com/@dviyer/mapping-our-social-change-roles-in-times-of-crisis-8bbe71a8ab01 - Success>
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/176/176/2*eIxJJxYO8Pv5fo6f2MHRJw.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/1*Aru1r2cATAyXdfWN-gD4Ig.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/1*PpgVLPJVt4PB66omfMs4Dw@2x.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/1*RyZypu-gN_qyxSa2cZabRQ.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/1*XPtf0bCcUJqmhrokVppiiA.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/1*eDtqX9EJSEqt0QDhYWSgGw.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/1*iTCl4mY2iqjaeh5uNIUFXg@2x.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/1*qsdCJc8JVH1hWX_RhgWfQA.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/2*BjnDHf7Nw0V2YZZG8uMm4w.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/2*I-jphmTgAk5nFhzoRhsqfQ.png ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/96/96/2*eIxJJxYO8Pv5fo6f2MHRJw.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*3PawtEP2XGEukHbO25gYeg.jpeg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*5653V50p3FtowC-6b2PNPA.jpeg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*IH_DjXGnoH_FHMSK43Uq2g.jpeg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*P29AoufJKJx2HVqKP30Fcg.jpeg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*QN0IRmH_ZzAkfiZiy4-o1g.jpeg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*Sf1P26awDZlwj9e5WfIbIQ.jpeg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*WEkUCm9Vd-Vc55r4APJupA.jpeg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*ct3FCxitC3nned4zSSY-ag.jpeg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*yt9ae_qciLvBcM6TgTx-cA.png ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/max/1400/1*HXIhNz9bKeHgq54DXx_2_w.png ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png ALT:TRUE)
│   │   │       └── ( ContentImage - https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png ALT:TRUE)
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14381 - Success>
│   │   │   └── <ExternalPage https://www.foundsf.org/index.php?title=STRIKE!..._Concerning_the_1968-69_Strike_at_San_Francisco_State_College - Success>
│   │   │       ├── ( ContentImage - /images/0/0e/Addressing-injustice.png ALT:TRUE)
│   │   │       ├── ( ContentImage - /images/1/18/Sfsuingl%24sfsu-strikers-march.jpg ALT:TRUE)
│   │   │       ├── ( ContentImage - /images/3/32/Sfsuingl%24sfsu-strikers-end-hayakawa.jpg ALT:TRUE)
│   │   │       ├── ( ContentImage - /images/5/56/Sfsuingl%24sfsu-riot-cop-line.jpg ALT:TRUE)
│   │   │       ├── ( ContentImage - /images/6/68/Sfsuingl%24hayakawa-at-podium.jpg ALT:TRUE)
│   │   │       ├── ( ContentImage - /images/7/77/On-strike-shut-it-down.jpg ALT:TRUE)
│   │   │       ├── ( ContentImage - /images/a/af/Sfsu-strike-crowd-on-entry-path_drescher.jpg ALT:TRUE)
│   │   │       ├── ( ContentImage - /images/f/fa/Tours-dissent.gif ALT:TRUE)
│   │   │       ├── ( ContentImage - /images/thumb/2/29/Sit-in2_for-web.jpg/720px-Sit-in2_for-web.jpg ALT:TRUE)
│   │   │       ├── ( ContentImage - /images/thumb/3/33/Sfsc_cafeteria-for-web.jpg/720px-Sfsc_cafeteria-for-web.jpg ALT:TRUE)
│   │   │       ├── ( ContentImage - /images/thumb/f/fd/Sit-in1_for-web.jpg/720px-Sit-in1_for-web.jpg ALT:TRUE)
│   │   │       ├── ( ContentImage - /index.php?title=File:Addressing-injustice.png ALT:FALSE)
│   │   │       ├── ( ContentImage - /index.php?title=File:On-strike-shut-it-down.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - /index.php?title=File:Sfsc_cafeteria-for-web.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - /index.php?title=File:Sfsu-strike-crowd-on-entry-path_drescher.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - /index.php?title=File:Sfsuingl$hayakawa-at-podium.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - /index.php?title=File:Sfsuingl$sfsu-riot-cop-line.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - /index.php?title=File:Sfsuingl$sfsu-strikers-end-hayakawa.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - /index.php?title=File:Sfsuingl$sfsu-strikers-march.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - /index.php?title=File:Sit-in1_for-web.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - /index.php?title=File:Sit-in2_for-web.jpg ALT:FALSE)
│   │   │       └── ( ContentURLVideo - https://www.youtube.com/embed/As_P3DueKrY?rel=0 - None - 2 )
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/asynchronous-assignments-percent-28things-to-complete-percent-29 - Success>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38731/ - business-to-do-list-flat-icon-modern-style-task-list-business-to-do-list-flat-icon-modern-style-any-purposes-perfect-web-138650221.jpg )>
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/asynchronous-assignments-percent-28things-to-read-and-watch-percent-29-3 - Success>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38739/ - collaboration.png )>
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/percent-c2-percent-a0-optional-resources-to-explore - Success>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38703/ - 25-10-19-survey-icon-set-1-color-7-.jpg )>
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/percent-c2-percent-a0-synchronous-session-agendas-percent-26-docs-percent-c2-percent-a0 - Success>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38699/ - kissclipart-icon-combine-together-clipart-computer-icons-colla-fa1be8078309bd5b.png )>
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/welcome-percent-2c-introductions-percent-26-our-teacher-identities-percent-c2-percent-a0day-1-of-the-institute - Success>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38705/ - @Lexx_Valdez Kids migration.jpg )>
│   │   └── ( ContentImage - /images/icons/mc-assignment-unpub.svg ALT:TRUE)
│   ├── <Module-3-Day2-Tuesday--August17th,2021>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14384 - Success>
│   │   │   └── <ExternalPage https://lab.cccb.org/en/henry-giroux-those-arguing-that-education-should-be-neutral-are-really-arguing-for-a-version-of-education-in-which-nobody-is-accountable/ - Success>
│   │   │       ├── ( ContentImage - https://lab.cccb.org/wp-content/uploads/IMG_20120308_162858-380x200.jpg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://lab.cccb.org/wp-content/uploads/Joao_França-150x150.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://lab.cccb.org/wp-content/uploads/educartecno_lab-380x200.jpg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://lab.cccb.org/wp-content/uploads/entrevistes-CCCB-380x200.png ALT:TRUE)
│   │   │       ├── ( ContentImage - https://lab.cccb.org/wp-content/uploads/giroux.jpg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://www.linkedin.com/shareArticle?mini=true&url=https://lab.cccb.org/en/henry-giroux-those-arguing-that-education-should-be-neutral-are-really-arguing-for-a-version-of-education-in-which-nobody-is-accountable/&title=Henry%20Giroux%3A%20%E2%80%9CThose%20arguing%20that%20education%20should%20be%20neutral%20are%20really%20arguing%20for%20a%20version%20of%20education%20in%20which%20nobody%20is%20accountable%E2%80%9D%20%7C%20CCCB%20Lab&summary=An interview with founder of critical pedagogy Henry Giroux on the meaning of education, suspicions regarding neutrality and on how current uncertainties could be a driving force to rethink and generate new possibilities.&source=CCCB Lab&submitted-image-url=https://lab.cccb.org/wp-content/uploads/giroux_lab-380x200.jpg ALT:FALSE)
│   │   │       ├── ( ContentURLVideo - https://www.cccb.org/en/multimedia/videos/hannah-arendt-the-art-of-reading-the-present/228115 - None - 3 )
│   │   │       └── ( ContentURLVideo - https://www.youtube-nocookie.com/embed/LCMXKt5vRQk?feature=oembed&iv_load_policy=3&modestbranding=1&rel=0&autohide=1&playsinline=1&showinfo=0&autoplay=0 - None - 3 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14386 - Success>
│   │   │   └── <ExternalPage https://www.methodspace.com/flux-pedagogy-transforming-teaching-learning-during-coronavirus/ - Success>
│   │   │       ├── ( ContentImage - https://images.squarespace-cdn.com/content/v1/606f09be9fd45e6380f33b68/1628249770058-A8UBID1UHGUNQO5DX9XD/SAGE+Publishing+Logo_r0+g51+b153_300ppi.png ALT:TRUE)
│   │   │       └── ( ContentURLVideo - https://www.youtube.com/channel/UCBvwezCD-116EczfhJIO5SQ - None - 3 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14390 - Success>
│   │   │   └── <ExternalPage https://docs.google.com/document/d/1VOJfjOzfxuHTbYBGSnc-zHCtuf9-oU-IQKiJ__0cY9E/edit# - Success>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14391 - Success>
│   │   │   └── <ExternalPage https://docs.google.com/presentation/d/1qb_9xRUMqw3d7ZwdYkRD_TFrNI4fyHV2-U5KJ9Ev63k/edit?usp=sharing - Success>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14392 - Success>
│   │   │   └── <ExternalPage https://docs.google.com/presentation/d/1P_AaBW_W3ElitD3W7MDQqDuPS8rHTXI7AJO7yVQuWew/edit#slide=id.p - Success>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14393 - Success>
│   │   │   └── <ExternalPage https://docs.google.com/document/d/1XvL14lVfRo2CYWnv-1n-BzZPvbXWOVPVXAj3M2cvEhE/edit - Success>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14394 - Success>
│   │   │   ├── ( ContentURLVideo - //www.youtube.com/embed/SFnMTHhKdkw - None - 3 )
│   │   │   └── ( ContentURLVideo - https://www.youtube.com/watch?v=SFnMTHhKdkw&t=17s - None - 3 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14395 - Success>
│   │   │   └── <ExternalPage https://docs.google.com/forms/d/1XNP1bsZ2satMl8cmdDlDepIk6hM7wxos9zzx2waLOBo/edit - Success>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14398 - Success>
│   │   │   └── <ExternalPage https://medium.com/@sfrising/what-sean-monterrosa-taught-us-his-teachers-7e7f7556956e - Success>
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/176/176/2*8ghxp0J7uX70TMYMg_Kscw.png ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/1*7t15Zc8v9ysnlfxCjugQ_w.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/1*DbLva6WYfvad54QfvBp_Iw.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/1*LklQCl-nB65QJ_EGGbR2aw.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/1*QIM6BG59L3AdLdwwNpRsSg.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/1*RTZhEFcTMR2utLIBk7nTiA.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/1*jzqIZtG5KWSKecJYPicsbg.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/1*p5k2w3ffwMVaxnjSzYvy_Q.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/2*ZoxOgCGeHFRpzzohIpaFRQ.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/40/40/2*ZrzTUNVzaUi86QPFH--w8g.jpeg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/fit/c/96/96/2*8ghxp0J7uX70TMYMg_Kscw.png ALT:TRUE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*8S0IiUzrdNIff4VK_GEBtg.jpeg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*US1D1iqA9SnXGVVTf0VxoA.jpeg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*Vd1n43p0fxtwVQkCFurZag.jpeg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*VqZprLd6drjjFfDn1R4sug.png ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*dpcoTYbxPLJwtkQlO4XXmQ.png ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*tgS-2bgGHivz8ccjVm_N1Q.jpeg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/focal/112/112/50/50/1*zyCyE_-dvC-GnaRzJnSwyA.jpeg ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/max/1152/1*_7qgZ67JxeOnGGixNpnNwQ.png ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/max/1370/1*NU3fQ_80c-DLQeXJ9d9ZeA.png ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/max/752/1*gBGo2x6wynYZZncHYp-nMw.png ALT:FALSE)
│   │   │       ├── ( ContentImage - https://miro.medium.com/max/892/1*42HA8R8pVmW4u79l6TmU1g.png ALT:FALSE)
│   │   │       └── ( ContentURLVideo - https://www.youtube.com/watch?v=A9n46bPFc34 - None - 3 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14399 - Success>
│   │   │   └── <ExternalPage https://www.theatlantic.com/ideas/archive/2021/05/whats-missing-from-the-discourse-about-anti-racist-teaching/618947/ - Success>
│   │   │       ├── ( ContentImage - https://cdn.theatlantic.com/assets/media/files/nav-crossword.png ALT:FALSE)
│   │   │       ├── ( ContentImage - https://cdn.theatlantic.com/media/files/YourSubscription_300x300.jpg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://cdn.theatlantic.com/media/files/archive-thumbnail.png ALT:TRUE)
│   │   │       ├── ( ContentImage - https://cdn.theatlantic.com/media/img/specialreports/lead/2020/10/14/Thumbnail.jpg ALT:TRUE)
│   │   │       ├── ( ContentImage - https://cdn.theatlantic.com/thumbor/sXP5Uo7KMMjH-rqZOpwB6yJUWCo=/0x0:4800x2700/960x540/media/img/mt/2021/05/anti_racist_teaching/original.jpg ALT:TRUE)
│   │   │       └── ( ContentImage - https://www.theatlantic.com/magazine/images/current-issue.large.jpg ALT:FALSE)
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14400 - Success>
│   │   │   ├── ( ContentURLVideo - //www.youtube.com/embed/39A0qBGb7WM - None - 3 )
│   │   │   └── ( ContentURLVideo - https://www.youtube.com/watch?v=39A0qBGb7WM - None - 3 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14401 - Success>
│   │   │   ├── ( ContentURLVideo - //www.youtube.com/embed/Q1cHoL4vaBs - None - 3 )
│   │   │   └── ( ContentURLVideo - https://www.youtube.com/watch?v=Q1cHoL4vaBs&t=118s - None - 3 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14402 - Success>
│   │   │   └── <ExternalPage https://www.vice.com/en_us/article/ywazwb/true-self-care-is-not-about-you - Success>
│   │   │       ├── ( ContentImage - https://video-images.vice.com/contributors/58ee5bfeed8d11643ad5e10a/lede/1529677175885-profilepic1.jpeg ALT:FALSE)
│   │   │       └── ( ContentURLVideo - https://www.youtube.com/user/vice - None - 3 )
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/asynchronous-assignments-percent-28things-to-read-and-watch-percent-29 - Success>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38739/ - collaboration.png )>
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/critical-pedagogies-percent-26-transformative-frameworksday-2-of-the-institute-goes-dee - Success>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38728/ - Octavia-Butler.jpg )>
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/percent-c2-percent-a0-optional-resources-to-explore-percent-28copy-percent-29 - Success>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38703/ - 25-10-19-survey-icon-set-1-color-7-.jpg )>
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/percent-c2-percent-a0-synchronous-session-agendas-percent-26-docs-percent-26nbspdotdotdot-percent-28copy-percent-29 - Success>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38699/ - kissclipart-icon-combine-together-clipart-computer-icons-colla-fa1be8078309bd5b.png )>
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/read-percent-3a-social-justice-frameworks-for-jigsaw-activity-please-read-the-1-article - Success>
│   │   │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38707/ - Designing Social Justice Education Courses.pdf )>
│   │   │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38718/ - the_four_is_of_oppression.pdf )>
│   │   │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38736/ - Resistance 101 Lesson Plan.pdf )>
│   │   │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38741/ - Socio-ecological Theory Lecture.pptx )>
│   │   │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38742/ - 8_1_2020_Breadth of.pdf )>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38743/ - mapping-margins.pdf )>
│   │   └── <Page https://sfsu.instructure.com/courses/330/pages/read-percent-3a-social-justice-frameworks-for-jigsaw-activity-please-read-the-1-article-2 - Success>
│   │       ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38707/ - Designing Social Justice Education Courses.pdf )>
│   │       ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38718/ - the_four_is_of_oppression.pdf )>
│   │       ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38736/ - Resistance 101 Lesson Plan.pdf )>
│   │       ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38741/ - Socio-ecological Theory Lecture.pptx )>
│   │       ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38742/ - 8_1_2020_Breadth of.pdf )>
│   │       └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38743/ - mapping-margins.pdf )>
│   ├── <Module-4-Day3-Wednesday--August18th,2021>
│   │   ├── <Discussion https://sfsu.instructure.com/courses/330/discussion_topics/1313 - Success>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14405 - Success>
│   │   │   └── <ExternalPage https://www.latimes.com/books/la-et-jc-decolonize-syllabus-20181008-story.html - Success>
│   │   │       └── ( ContentURLVideo - https://www.youtube.com/losangelestimes - None - 4 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14406 - Success>
│   │   │   └── <ExternalPage https://docs.google.com/document/d/1t0VyANpJ2oZvF5Up7on8lCvx0KTX3DQPYN0L6CHCIzA/edit - Success>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14416 - Success>
│   │   │   └── <ExternalPage https://docs.google.com/forms/d/17ILlWWENP5kgekYjd-_iW1cJVzmhnhhjkxZ0MPyBZSs/edit - Success>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14417 - Success>
│   │   │   └── <ExternalPage https://sfsu.co1.qualtrics.com/jfe/form/SV_2i55pxOMiLuDoMd - Success>
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14420 - Success>
│   │   │   ├── ( ContentURLVideo - //www.youtube.com/embed/aMrf_MC5COk - None - 4 )
│   │   │   └── ( ContentURLVideo - https://www.youtube.com/watch?v=aMrf_MC5COk&list=PLcYQvzieEOdSfUWowBqZPVhrbEVw9jceg&index=28 - None - 4 )
│   │   ├── <Item https://sfsu.instructure.com/courses/330/modules/items/14421 - Success>
│   │   │   └── <ExternalPage https://ueap.sfsu.edu/exco - Success>
│   │   │       └── ( ContentImage - /sites/default/files/styles/sf_state_1920x400/public/images/EXCO_Hero.jpg ALT:FALSE)
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/asynchronous-assignments-percent-28things-to-read-and-watch-percent-29-2 - Success>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38739/ - collaboration.png )>
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/asynchronous-percent-2fsynchronous-assignments-percent-28things-to-explore-and-percent-2for-createdot-y - Success>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38731/ - business-to-do-list-flat-icon-modern-style-task-list-business-to-do-list-flat-icon-modern-style-any-purposes-perfect-web-138650221.jpg )>
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/course-curriculum-developmentday-3-of-the-institute-is-all-about-applicationdot - Success>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38709/ - Masters tools- Lorde.jpg )>
│   │   ├── <Page https://sfsu.instructure.com/courses/330/pages/percent-c2-percent-a0-optional-resources-to-explore-percent-28copy-percent-29-percent-28copy-percent-29 - Success>
│   │   │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38703/ - 25-10-19-survey-icon-set-1-color-7-.jpg )>
│   │   └── <Page https://sfsu.instructure.com/courses/330/pages/percent-c2-percent-a0-synchronous-session-agendas-percent-26-docs-percent-26nbspdotdotdot-percent-28copy-percent-29-percent-28copy-percent-2 - Success>
│   │       └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38699/ - kissclipart-icon-combine-together-clipart-computer-icons-colla-fa1be8078309bd5b.png )>
│   └── <Module-5-Archive>
│       └── <Page https://sfsu.instructure.com/courses/330/pages/untitled-page - Success>
│           └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38713/ - download.jpg )>
└── <Pages https://sfsu.instructure.com/courses/330/pages - Success>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/asynchronous-assignments-percent-28things-to-complete-percent-29 - Success>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38731/ - business-to-do-list-flat-icon-modern-style-task-list-business-to-do-list-flat-icon-modern-style-any-purposes-perfect-web-138650221.jpg )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/asynchronous-assignments-percent-28things-to-read-and-watch-percent-29 - Success>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38739/ - collaboration.png )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/asynchronous-assignments-percent-28things-to-read-and-watch-percent-29-2 - Success>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38739/ - collaboration.png )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/asynchronous-assignments-percent-28things-to-read-and-watch-percent-29-3 - Success>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38739/ - collaboration.png )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/asynchronous-percent-2fsynchronous-assignments-percent-28things-to-explore-and-percent-2for-createdot-y - Success>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38731/ - business-to-do-list-flat-icon-modern-style-task-list-business-to-do-list-flat-icon-modern-style-any-purposes-perfect-web-138650221.jpg )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/community-builders - Success>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38744/ - Human Bingo.doc )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/course-curriculum-developmentday-3-of-the-institute-is-all-about-applicationdot - Success>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38709/ - Masters tools- Lorde.jpg )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/critical-pedagogies-percent-26-transformative-frameworksday-2-of-the-institute-goes-dee - Success>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38728/ - Octavia-Butler.jpg )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/percent-c2-percent-a0-optional-resources-to-explore - Success>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38703/ - 25-10-19-survey-icon-set-1-color-7-.jpg )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/percent-c2-percent-a0-optional-resources-to-explore-percent-28copy-percent-29 - Success>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38703/ - 25-10-19-survey-icon-set-1-color-7-.jpg )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/percent-c2-percent-a0-optional-resources-to-explore-percent-28copy-percent-29-percent-28copy-percent-29 - Success>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38703/ - 25-10-19-survey-icon-set-1-color-7-.jpg )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/percent-c2-percent-a0-our-schedule-percent-c2-percent-a0tuesday-percent-2c-august-16thwednesday-percent-2c-august-17th-percent-c2-percent-a0thu - Success>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/percent-c2-percent-a0-synchronous-session-agendas-percent-26-docs-percent-26nbspdotdotdot-percent-28copy-percent-29 - Success>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38699/ - kissclipart-icon-combine-together-clipart-computer-icons-colla-fa1be8078309bd5b.png )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/percent-c2-percent-a0-synchronous-session-agendas-percent-26-docs-percent-26nbspdotdotdot-percent-28copy-percent-29-percent-28copy-percent-2 - Success>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38699/ - kissclipart-icon-combine-together-clipart-computer-icons-colla-fa1be8078309bd5b.png )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/percent-c2-percent-a0-synchronous-session-agendas-percent-26-docs-percent-c2-percent-a0 - Success>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38699/ - kissclipart-icon-combine-together-clipart-computer-icons-colla-fa1be8078309bd5b.png )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/read-percent-3a-social-justice-frameworks-for-jigsaw-activity-please-read-the-1-article - Success>
    │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38707/ - Designing Social Justice Education Courses.pdf )>
    │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38718/ - the_four_is_of_oppression.pdf )>
    │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38736/ - Resistance 101 Lesson Plan.pdf )>
    │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38741/ - Socio-ecological Theory Lecture.pptx )>
    │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38742/ - 8_1_2020_Breadth of.pdf )>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38743/ - mapping-margins.pdf )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/read-percent-3a-social-justice-frameworks-for-jigsaw-activity-please-read-the-1-article-2 - Success>
    │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38707/ - Designing Social Justice Education Courses.pdf )>
    │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38718/ - the_four_is_of_oppression.pdf )>
    │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38736/ - Resistance 101 Lesson Plan.pdf )>
    │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38741/ - Socio-ecological Theory Lecture.pptx )>
    │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38742/ - 8_1_2020_Breadth of.pdf )>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38743/ - mapping-margins.pdf )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/untitled-page - Success>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38713/ - download.jpg )>
    ├── <Page https://sfsu.instructure.com/courses/330/pages/welcome-percent-21 - Success>
    │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38704/ - celestebyers_justicefirst.jpg )>
    │   ├── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38722/ - Screen Shot 2020-08-03 at 12.40.30 PM.png )>
    │   └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38740/ - Savi 1.jpg )>
    └── <Page https://sfsu.instructure.com/courses/330/pages/welcome-percent-2c-introductions-percent-26-our-teacher-identities-percent-c2-percent-a0day-1-of-the-institute - Success>
    └── ( ContentCanvasFile - https://sfsu.instructure.com/courses/330/files/38705/ - @Lexx_Valdez Kids migration.jpg )>

````