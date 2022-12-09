import streamlit as st
import streamlit_book as stb

st.markdown("""
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css"/>
<!-- Swiper CSS -->
<link rel="stylesheet" href="css/swiper-bundle.min.css" />
<!-- CSS -->
<link rel="stylesheet" href="css/style.css" />
<!-- Boxicons CSS -->
<link href=" https://unpkg.com/boxicons@2.1.2/css/boxicons.min.css" rel="stylesheet" />
</head>

<style>
.button {
  border: none;
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}

h1{
  text-align: center;
}

.button1 {
  background-color: white; 
  color: black; 
  border: 2px solid #990000;
  align-items: center;
  display: inline-block;
  display: block;     
  width: 200px;
}  

.margin-auto {    
  margin: 0 auto;
}

.button1:hover {
  background-color: #990000;
  color: white;
}


.center {
margin: 0;
position: absolute;
top: 150%;
left: 20%;
-ms-transform: translate(-50%, -50%);
transform: translate(-50%, -50%);
}


.center2 {
margin: 0;
position: absolute;
top: 150%;
left: 80%;
-ms-transform: translate(-50%, -50%);
transform: translate(-50%, -50%);
}

.button2 {
  background-color: white; 
  color: black; 
  border: 2px solid #990000;
  align-items: center;
  display: inline-block;
  display: block;     
  width: 200px;
}  

.button2:hover {
  background-color: #990000;
  color: white;
}

.center-image {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  height: 50%;
}

.elementor-image{
  width: 25%;
  float: left;
}
.main {
  width: 75%;
  float: left;
}


.title {
  color: grey;
  font-size: 18px;
}

button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}

button:hover, a:hover {
  opacity: 0.7;
}

/* card styles*/


@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');
*{
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}
::selection{
  background: #8e44ad;
  color: #fff;
}
html,body{
  display: grid;
  height: 100%;
  place-items: center;
  background: #8e44ad;
}
.container{
  max-width: 1100px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  padding: 20px;
}
.container .box{
  width: calc(33% - 10px);
  background: #fff;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px 30px;
  border-radius: 5px;
}
.box .quote i{
margin-top: 10px;
font-size: 45px;
color: #17c0eb
}
.container .box .image{
  margin: 10px 0;
  height: 150px;
  width: 150px;
  background: #bd1111;
  padding: 3px;
  border-radius: 50%;
}
.box .image img{
  height: 100%;
  width: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #fff;
}
.box p{
  text-align: justify;
  margin-top: 8px;
  font-size: 16px;
  font-weight: 400;
}
.box .name_job{
  margin: 10px 0 3px 0;
  color: #bd1111;
  font-size: 18px;
  font-weight: 600;
  text-align: center;
}
.rating i{
  font-size: 18px;
  color: #8e44ad;
  margin-bottom: 5px;
}
.btns{
  margin-top: 20px;
  margin-bottom: 5px;
  display: flex;
  justify-content: space-between;
  width: 100%;
}
.btns button{
  background: #8e44ad;
  width: 100%;
  padding: 9px 0px;
  outline: none;
  border: 2px solid #8e44ad;
  border-radius: 5px;
  cursor: pointer;
  font-size: 18px;
  font-weight: 400;
  color: #8e44ad;
  transition: all 0.3s linear;
}
.btns button:first-child{
  background: none;
  margin-right: 5px;
}
.btns button:last-child{
  color: #fff;
  margin-left: 5px;
}
.btns button:first-child:hover{
  background: #8e44ad;
  color: #fff;
}
.btns button:hover{
  color: #fff;
}
@media (max-width:1045px){
  .container .box{
    width: calc(50% - 10px);
    margin-bottom: 20px;
  }
}
@media (max-width:710px){
  .container .box{
    width: 100%;
  }
}
/* testimonials */
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}
html,body{
  display: grid;
  height: 100%;
  place-items: center;
  background: #17a2b8;
}
::selection{
  background: rgba(23,162,184,0.3);
}
.wrapper{
  max-width: 1200px;
  margin: auto;
  padding: 0 20px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
}
.wrapper .box{
  background: #fff;
  width: calc(33% - 10px);
  padding: 25px;
  border-radius: 3px;
  box-shadow: 0px 4px 8px rgba(0,0,0,0.15);
}
.wrapper .box i.quote{
  font-size: 20px;
  color: #ff4d4d;
}
.wrapper .box .content{
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  padding-top: 10px;
}
.box .info .name{
  font-weight: 600;
  font-size: 17px;
}
.box .info .job{
  font-size: 16px;
  font-weight: 500;
  color: #ff4d4d;
}
.box .info .stars{
  margin-top: 2px;
}
.box .info .stars i{
  color: #ff4d4d;
}
.box .content .image{
  height: 75px;
  width: 75px;
  padding: 3px;
  background: #17a2b8;
  border-radius: 50%;
}
.content .image img{
  height: 100%;
  width: 100%;
  object-fit: cover;
  border-radius: 50%;
  border: 2px solid #fff;
}
.box:hover .content .image img{
  border-color: #fff;
}
@media (max-width: 1045px) {
  .wrapper .box{
    width: calc(50% - 10px);
    margin: 10px 0;
  }
}
@media (max-width: 702px) {
  .wrapper .box{
    width: 100%;
  }
}
 /*sponsers*/
.container-sp{
    padding-top: 50px;
    margin-bottom:180px;
}
h2{
    text-align: center;
    padding: 20px;
}
.slick-slide{
    margin: 0 20px;
}
.slick-slide img{
    width: 100%;
}
.slick-slider{
    position: relative;
    display: block;
    box-sizing: border-box;
}
.slick-list{
    position: relative;
    display: block;
    overflow: hidden;
    margin: 0;
    padding: 0;
}
.slick-track{
    position: relative;
    top: 0;
    left: 0;
    display: block
}
.slick-slide{
    display: none;
    float: left;
    height: 100%;
    min-height: 1px;
}
.slick-slide img{
    display: block;
}
.slick-initialized .slick-slide{
    display: block;
}
.copy{
    padding-top: 250px;
}
.image{
    padding: 14px 20px;
    margin:10px;
    width:120px;
    height:120px;
    float: left;
}
</style>

</head>
<body>

<img class="center-image" 
src="https://www.mailgenius.com/wp-content/uploads/2021/02/consulting.png">
<h1>About Us</h1>
<div class="elementor-testimonial-content">
<span class="h">Bitwalls was fantastic</span> in helping our company resolve many issues we encountered with email deliverability.
They did a deep dive into our account running many tests and helped implement the most up to date best practices to ensure our emails could now be delivered to our customers. 
<span class="h">They work with a fantastic array of tools to help get the job done and assisted in setting up automation for our SPF records, highly recommended!
</span>
</div>

<div class="container-sp">
    <h2 class="text-center font-weight-bold">Our Partners</h2>
    <section class="customer-logos slider">
        <div class="slide"><img class="image" src="https://cdn-icons-png.flaticon.com/512/5968/5968534.png" alt="logo"></div>
        <div class="slide"><img  class="image" src="https://cdn-icons-png.flaticon.com/512/732/732223.png" alt="logo"></div>
        <div class="slide"><img class="image" src="https://cdn-icons-png.flaticon.com/512/2504/2504961.png" alt="logo"></div>
        <div class="slide"><img class="image" src="https://www.edigitalagency.com.au/wp-content/uploads/new-mailchimp-logo-vertical-black.png" alt="logo"></div>
        <div class="slide"><img class="image" src="https://sendgrid.com/wp-content/themes/sgdotcom/pages/resource/brand/2016/SendGrid-Logomark.png" alt="logo"></div>   
    </section>
</div>
<div>
<h3 style="text-align: center;">A few of our Testimonials</h3>
<br><br>
<div class="wrapper">
    <div class="box">
      <i class="fas fa-quote-left quote"></i>
      <p>"My experience with Bitwalls was amazing - beyond 5 stars. The service is great and I have seen returns immediately. Within one consulting session, we went over so much that I made my money back tenfold."</p>
      <div class="content">
        <div class="info">
          <div class="name">Alex Smith</div>
          <div class="job">Designer | Developer</div>
          <div class="stars">
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="far fa-star"></i>
            <i class="far fa-star"></i>
            <i class="far fa-star"></i>
          </div>
        </div>
      </div>
    </div>
    <div class="box">
      <i class="fas fa-quote-left  quote"></i>
      <p>"I'd recommend MailGenius to everyone. Amazingly knowledgeable about email deliverability. I got a sneak peak at their new tool, and it's absolutely fantastic."</p>
      <div class="content">
        <div class="info">
          <div class="name">Kristina Bellis</div>
          <div class="job">Freelancer | Advertiser</div>
          <div class="stars">
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="far fa-star"></i>
          </div>
        </div>
      </div>
    </div>
  </div>

<br><br>


<!---cards --!>
<h3 style="text-align: center;">BitWalls Development Team</h3>
<div class="container">
  <div class="box">
    <div class="image">
        <img src="https://scontent.fcmb1-2.fna.fbcdn.net/v/t1.6435-9/176187504_749856492387633_6592715076216757190_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=174925&_nc_eui2=AeGvBjsfD2P4QXlgHU_Ut2EszwEGABwryUrPAQYAHCvJStCUonK5H5Y1cx1Nczg5r1uJqq-Sq_YnPWZaF90DJHLg&_nc_ohc=Ym8uvllaIuIAX8IzKuI&_nc_ht=scontent.fcmb1-2.fna&oh=00_AfBG5EjRM2BvlDWUqN2V_E3STFmhgNMJt5sM_vbL7IqLqg&oe=63BA048B">
    </div>
  <div class="name_job">Pasindu Bandara</div>
  <div class="name_job">IT20021252</div>
  </div>
  
 <div class="box">
    <div class="image">
        <img src="https://scontent.fcmb1-2.fna.fbcdn.net/v/t39.30808-6/274873973_3097902847204313_7595800818736764616_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=174925&_nc_eui2=AeHIrY0yqW2qlyTN1HF12dBcyfHpg4kFn6nJ8emDiQWfqanWy2weA3hHpQ8nGWCyzLQMAuh1YFXUPKJvkr5kmDSL&_nc_ohc=mUEWRQvG7M4AX_CzNqT&_nc_ht=scontent.fcmb1-2.fna&oh=00_AfBTahBq9iFAK5uxWLyB9EY3n04r-cFgRiogrhaNoTcUtg&oe=63985BF1">
    </div>
 <div class="name_job">Hansa Ranaweera</div>
 <div class="name_job">IT20012960</div>
 </div>
    
</div>

</body>""", unsafe_allow_html=True)