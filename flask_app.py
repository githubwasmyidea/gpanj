from flask import Flask, render_template_string, request
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from io import BytesIO
from datetime import datetime
app = Flask(__name__)
import pytz

def getDatatable():
    df2=pd.read_excel("data.xlsx")
    with open('error.txt', 'r') as file:
        error=file.read()
    with open('last_updated.txt','r') as file2:
        last_updated=file2.read()
    return df2,error,last_updated

@app.route('/', methods=['GET', 'POST'])
def home():
    df2,sd,last_updated = getDatatable()
    #print(df2)
    # Handle search query
    query = request.args.get('query')
    if query:
        df2 = df2[df2.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    #df2 = pd.concat([df2] * 50, ignore_index=True)
    # = datetime.now(pytz.utc)
    #eastern = pytz.timezone('US/Eastern')
    #last_updated = utc_now.astimezone(eastern).strftime("%m-%d-%Y %H:%M:%S")
    table_html = df2.to_html(index=False, classes='table table-striped', escape=False)

    return render_template_string('''
    <!DOCTYPE html>

    <!-- Menus Loaded --><!-- Input Shortener Loaded --><!-- Slideshows Loaded --><!-- SVG Icons Loaded -->
    <!-- News Feed Loaded -->
    <!-- Event Feed Loaded --><!-- RSS News Feed Loaded --><!-- Recent Event Feed Loaded --><!-- Member Feed Loaded --><!-- Functions Loaded --><html lang="en">
    	<head>
    		<title>Exclusion List - Governmental Purchasing Association of New Jersey</title>
    		<meta name="keywords" content="" />
    		<meta name="description" content="" />
    		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
    		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    		<link rel="icon" type="image/svg+xml" href="https://gpanj.com/images/favicon.svg">
    		<link rel="alternate icon" href="https://gpanj.com/images/favicon.png">
    		<link rel="stylesheet" type="text/css" href="https://gpanj.com/bootstrap/css/bootstrap.min.css" />
    		<link rel="stylesheet" type="text/css" href="https://gpanj.com/_jquery/css/custom-theme/jquery-ui-1.9.2.custom.min.css" />
    		<link rel="stylesheet" type="text/css" href="https://gpanj.com/_jquery/css/jquery.ui.potato.menu.css" />
    		<link rel="stylesheet" type="text/css" href="https://gpanj.com/_jquery/css/fullcalendar.css" />
    		<link rel="stylesheet" type="text/css" href="https://gpanj.com/_jquery/css/fullcalendar.print.css" media="print" />
    		<script type="text/javascript" src="https://gpanj.com/_jquery/js/jquery-1.10.1.min.js"></script>
    		<script type="text/javascript" src="https://gpanj.com/_jquery/js/jquery-migrate-1.2.1.min.js"></script>
    		<script type="text/javascript" src="https://gpanj.com/_jquery/js/jquery-ui-1.9.2.custom.min.js"></script>
    		<script type="text/javascript" src="https://gpanj.com/_jquery/js/jquery.jpanelmenu.min.js"></script>
    		<script src="//memberleap.com/_jquery/fullcalendar-1.5.3/fullcalendar/fullcalendar.min.js"></script>
    		<!-- Google ReCaptcha -->
    		<script src='https://www.google.com/recaptcha/api.js'></script>

    		<!--[if lt IE 9]>
    			<script type="text/javascript" src="https://gpanj.com/_jquery/js/html5shiv.js?ccccombo_breaker="></script>
    			<script type="text/javascript" src="https://gpanj.com/_jquery/js/respond.min.js?ccccombo_breaker="></script>
    			<script type="text/javascript" src="https://gpanj.com/_jquery/js/modernizr.custom.36944.js?ccccombo_breaker="></script>

    		<![endif]-->
    		<script type="text/javascript" src="https://gpanj.com/_jquery/js/fullcalendar.min.js"></script>
    		<script type="text/javascript" src="https://gpanj.com/bootstrap/js/bootstrap.min.js"></script>
    		<script type="text/javascript" src="https://gpanj.com/_jquery/js/_custom.js"></script>
    		<link href="https://www.viethconsulting.com/_jquery/nivo/nivo-slider.css" media="screen" rel="stylesheet" type="text/css">

    		<!-- Jake jquery bits -->
    				<!-- Google fonts -->
    		<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lora:wght@500&family=Mulish:wght@400;600;700&display=swap" rel="stylesheet">		<!-- ^^ Enter this in config.php -->

    		<!-- Our style sheets -->
    		<!--##MH5INJECTS-->
    		<!-- ^^This injects MMS specific styles -->
    		<link rel="stylesheet" type="text/css" href="https://gpanj.com/css/navigation.css?combobreaker=1554176871" />
    		<link rel="stylesheet" type="text/css" href="https://gpanj.com/css/style.css?combobreaker=1523392544" />



    		<!--[if lt IE 9]>
    		<script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
    		<style type="text/css">
    				body{
    					background-repeat: repeat;
    				}
    				.navbar-toggle{
    					display: none;
    				}
    				.ie8mademedoit{
    					margin-top: 20px;
    				}
    			</style>
    		<![endif]-->
    	</head>
    	<body>
    		<div id="fb-root"></div>
    		<script>(function(d, s, id) {
    		  var js, fjs = d.getElementsByTagName(s)[0];
    		  if (d.getElementById(id)) return;
    		  js = d.createElement(s); js.id = id;
    		  js.src = 'https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.2';
    		  fjs.parentNode.insertBefore(js, fjs);
    		}(document, 'script', 'facebook-jssdk'));</script><div id="mobileMenuWrapper"><ul id="mobile-menu"><li id="triggerClose" class="mobileMenuTrigger">+</li>
    				 <li><a href="https://gpanj.com/" class="home-link">Home</a></li><li><a href="#" class="mToggle">About GPANJ<b class="caret"></b></a><ul class="mDropdown"><li><a href="https://www.gpanj.com/presidents_message.php" target="_top">President's Message</a></li><li><a href="https://www.gpanj.com/mission.php" target="_top">Mission</a></li><li><a href="https://www.gpanj.com/GPAN_FA_LIST_10396455.php" target="_top">General Information</a></li></ul></li><li><a href="#" class="mToggle">Membership<b class="caret"></b></a><ul class="mDropdown"><li><a href="https://www.gpanj.com/members_login.php" target="_top">Members Login</a></li><li><a href="https://members.gpanj.com/members/newmem/new-mem-reg.php?org_id=GPAN" target="_blank">Membership Application</a></li><li><a href="https://www.gpanj.com/member_benefits.php" target="_top">Member Benefits</a></li></ul></li><li><a href="#" class="mToggle">Education<b class="caret"></b></a><ul class="mDropdown"><li><a href="https://www.gpanj.com/courses.php" target="_top">Courses</a></li><li><a href="https://chapter7nigp.org/" target="_top">NIGP - Chapter 7</a></li></ul></li><li><a href="https://members.gpanj.com/members/calendar6c_responsive.php?org_id=GPAN" target="_top">Events</a></li><li><a href="#" class="mToggle">Mini-Conference 2024<b class="caret"></b></a><ul class="mDropdown"><li><a href="https://www.gpanj.com/GPAN_FA_LIST_10423339.php" target="_top">Information</a></li></ul></li><li><a href="https://www.gpanj.com/resources.php" target="_top">Resources</a></li><li><a href="#" class="mToggle">Specification Library<b class="caret"></b></a><ul class="mDropdown"><li><a href="https://members.gpanj.com/members/secure/filearchive/filelist.php?fac=8406" target="_top">Goods & Services</a></li><li><a href="https://members.gpanj.com/members/secure/filearchive/filelist.php?fac=8407" target="_top">Construction</a></li></ul></li><li><a href="https://www.gpanj.com/contact_us.php" target="_top">Contact Us</a></li></ul></div><script type="text/javascript">
    	$(function(){
    		var $trigger = $('.mobileMenuTrigger');
    		var $target  = $('#mobileMenuWrapper');
    		$trigger.click(function(e){
    			$target.toggleClass('open');
    			e.stopPropagation();
    		});
    		//Handles menu hide/show
    		$(".mToggle").click(function(e){
    			$(this).siblings("ul.mDropdown").toggleClass("open");
    			e.stopPropagation();
    		});
    		$("body").click(function(e){
    			clicked = $(e.target);
    			//console.log(clicked);
    			var pass = true;
    			if(clicked.parents("#mobile-menu").length){
    				pass = false;
    			}
    			if(!$target.hasClass("open")){
    				pass = false;
    				//console.log("this");
    			}
    			//console.log(pass);
    			if(pass == true){
    				e.stopPropagation();
    				$target.toggleClass('open');
    			}
    		});

    		//

    	});
    </script>
    <!-- Start of Member Login Modal -->
    <div class="modal fade" id="login-modal" tabindex="-1" role="dialog" aria-labelledby="login-modalLabel" aria-hidden="true">
    	<div class="modal-dialog">
    		<div class="modal-content">
    			<div class="modal-header">
    				<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
    				<h4 class="modal-title" id="login-modalLabel">Member Log In</h4>
    			</div>
    			<div class="modal-body">

    	<form action="https://members.gpanj.com/members/gateway.php" method="post" class="login-form">
    		<input type="hidden" name="org_id" value="GPAN" />
    		<div>
    		 <input name="Username" type="text" placeholder="Username" class="" />
    		</div><div>
    		 <input name="Password" type="password" placeholder="Password" class="" />
    		</div>
    		<a class="" href="http://gpanj.com/forgot_pwd.php">Forgot Password?</a>
    		<input type="submit" value="Sign In" class="" />


    	</form>
    				</div>
    		</div>
    	</div>
    </div>
    <!-- End of Member Login Modal -->
    <header>

    	<section class="header-bottom wrapper">
    		<a href="https://gpanj.com/">
    			<img src="https://gpanj.com/images/main-logo.png" alt="" class="img-responsive">
    		</a>
    		<button aria-label="Menu" class="mobileMenuTrigger visible-xs visible-sm">
    			<svg id="burger-menu" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.11 20"><defs><style>svg#burger-menu .cls-1{fill:#151a3d;}</style></defs><g id="Layer_2" data-name="Layer 2"><g id="Resources"><rect class="cls-1" width="30.11" height="3.35" rx="1.67"/><rect class="cls-1" y="8.33" width="30.11" height="3.35" rx="1.67"/><rect class="cls-1" y="16.65" width="30.11" height="3.35" rx="1.67"/></g></g></svg>		</button>
    	</section>
    	<section class="header-menu wrapper">
    		<nav>
    			<div id="nav_menu" class="NP collapse navbar-collapse navbar-ex1-collapse"><ul class="nav navbar-nav men-level-"><li id="triggerClose" class="mobileMenuTrigger">+</li>
    				 <li><a href="https://gpanj.com/" class="home-link">Home</a></li><li class="dropdown t "><a href="#" class="dropdown-toggle" data-toggle="dropdown">About GPANJ<b class="caret"></b></a><ul class="dropdown-menu men-level-"><li><a href="https://www.gpanj.com/presidents_message.php" target="_top">President's Message</a></li><li><a href="https://www.gpanj.com/mission.php" target="_top">Mission</a></li><li><a href="https://www.gpanj.com/GPAN_FA_LIST_10396455.php" target="_top">General Information</a></li></ul></li><li class="dropdown t0 "><a href="#" class="dropdown-toggle" data-toggle="dropdown">Membership<b class="caret"></b></a><ul class="dropdown-menu men-level-0"><li><a href="https://www.gpanj.com/members_login.php" target="_top">Members Login</a></li><li><a href="https://members.gpanj.com/members/newmem/new-mem-reg.php?org_id=GPAN" target="_blank">Membership Application</a></li><li><a href="https://www.gpanj.com/member_benefits.php" target="_top">Member Benefits</a></li></ul></li><li class="dropdown t0 "><a href="#" class="dropdown-toggle" data-toggle="dropdown">Education<b class="caret"></b></a><ul class="dropdown-menu men-level-0"><li><a href="https://www.gpanj.com/courses.php" target="_top">Courses</a></li><li><a href="https://chapter7nigp.org/" target="_top">NIGP - Chapter 7</a></li></ul></li><li><a href="https://members.gpanj.com/members/calendar6c_responsive.php?org_id=GPAN" target="_top">Events</a></li><li class="dropdown t0 "><a href="https://www.gpanj.com/resources.php" target="_top">Resources</a></li><li class="dropdown t0 "><a href="#" class="dropdown-toggle" data-toggle="dropdown">Specification Library<b class="caret"></b></a><ul class="dropdown-menu men-level-0"><li><a href="https://members.gpanj.com/members/secure/filearchive/filelist.php?fac=8406" target="_top">Goods & Services</a></li><li><a href="https://members.gpanj.com/members/secure/filearchive/filelist.php?fac=8407" target="_top">Construction</a></li></ul></li><li><a href="https://www.gpanj.com/contact_us.php" target="_top">Contact Us</a></li></ul></div><script type="text/javascript">
    		$('ul.dropdown-menu [data-toggle=dropdown]').on('click', function(event) {
    			event.preventDefault();
    			event.stopPropagation();
    			$(this).parent().toggleClass('open');
    			var menu = $(this).parent().find("ul");
    			var menupos = menu.offset();

    			if ((menupos.left + menu.width()) + 30 > $(window).width()) {
    				var newpos = - menu.width();
    			} else {
    				var newpos = $(this).parent().width();
    			}
    			menu.css({ left:newpos });
    		});
    		function checkForChanges(){
    			if (!$('.navbar-collapse').hasClass('in')){
    				$('.nav-row').css('max-height','40px');
    			} else {
    				$('.nav-row').css('max-height','none');
    				setTimeout(checkForChanges, 500);
    			}
    		}
    		$(function(){
    			checkForChanges();
    		});
    	</script>		</nav>
    	</section>
    </header>


    <!-- <div class="container"> -->
    <!--######################################################### table data ########################################-->
    <main id="subpage-main" class="container">
    					<div class="row">
    						<div class="col-md-12">
    							<h1 class="title">Exclusion List</h1>

    <body>
        <div class="container">

            <form method="get" action="/">
                <div class="form-group">
                    <input type="text" name="query" class="form-control" placeholder="Search..." value="{{ request.args.get('query', '') }}">
                </div>
                <button type="submit" class="btn btn-primary">Search</button>
                <p>Last updated: {{ last_updated }}, Error: {{sd}}</p>
            </form>
            <div class="table-wrapper">
                {{ table_html | safe }}
            </div>
        </div>
    </body>

    </main>
    <!-- ##################################################table data ends ######################################################-->
    <footer class="wrapper">
    	<div class="text-left">
    		<p>
    			Copyright &copy; 2024 <strong>Governmental Purchasing Association of New Jersey</strong>
    			<br>
    			All rights reserved. Website powered by <a href="https://www.memberleap.com" target="_blank">MemberLeap.</a>
    		</p>
    	</div>
    	<div class="text-right">
    		<p><a href="https://gpanj.com/privacy_policy.php">Privacy Policy</a></p>
    	</div>
    </footer>
    </div> <!-- Closes .container from header -->


    </body>
    </html>




    ''', table_html=table_html,last_updated=last_updated,sd=sd)

if __name__ == "__main__":
    app.run(debug=True)
