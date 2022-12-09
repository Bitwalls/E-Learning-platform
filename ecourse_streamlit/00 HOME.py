import streamlit as st
import streamlit_book as stb
from PIL import Image, ImageEnhance

# Add the title for the e-tutorial
st.markdown("""<style>


h1{
  text-align: center;
}

/* This is button for spam email detector */

.button{
   background-color:#EF432F; 
   border-radius: 8px;
   border:none;
   padding: 14px 25px;
   font-size:15px;
   text-align: center;
}

.button1 a,.button3 a{
  text-decoration: none;
  color: white;
  padding: 14px 25px;
  display: inline-block;
}

.button2 a{
    text-decoration:none;
    color:white;
    font-size:15px;
    padding: 14px 25px;
    display: inline-block;

}

.margin-auto {    
  margin: 0 auto;
}

.button1:hover, .button2:hover, .button3:hover{
  background-color: #B42117;
}


.center {
margin: 0;
position: absolute;
top: 120%;
left: 20%;
-ms-transform: translate(-50%, -50%);
transform: translate(-50%, -50%);
}
/* This is button for quiz  */

.button2 {
  align-items: center;
  
  display: block;     
  width: 200px;
}  

.center2 {
margin: 0;
position: absolute;
top: 120%;
left: 50%;
-ms-transform: translate(-50%, -50%);
transform: translate(-50%, -50%);
}

.button3 {
  align-items: center;
  display: inline-block;
  display: block;     
  width: 200px;
}  

.center3 {
margin: 0;
position: absolute;
top: 120%;
left: 80%;
-ms-transform: translate(-50%, -50%);
transform: translate(-50%, -50%);
}

.center-image {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 70%;
  height: 70%;
}

</style>

<body>
<img class="center-image" src="https://lh3.googleusercontent.com/yf_qekgBdN7kNFlG7CQJFhx8rl0Qa44sxnX8_tXo30HRU75ZnQtk1oe6GulNL6MlR9SKi1NEA7DAMLQpjRQfUK1BIqpkrEhssY264m5QMEt0hb9cwSkwjHtcsrTnO_FXfq2Pey-5aBPIiWhTZ_Ry_O63StdoDbV167zpL-HsztOfHe6Eg2WqcKhxLvj3bavJiXoFhxWxmz-8b77gVQV-fCDUcE1-7sweup8FuvsORX4LM82dI5X7nuJKUls-V9GIjxAwqIdlST0Uo3jroCnExoOtxp5OjMUb_fZzD16DQ5y3IOfNePEyY_h0hO6jaaqJu1G7bSG2HlJww8LwbIbaogoCuY6hnga7FGI_oCFewleXqLoLTHD5XHTL0OM5SXxlwD1yQzMW4QPsNFCZ69PTj64M3zETfstunERou90yh2028P_x0z8sIAHfY8GKqh5ehflr9yVoV_jaS33v3nmtlCKG9eK6gItHn6xcgAo49jVqcAMLmrjRSJVSJAHw7p_oVfz4-wxn1YNbPsnFtcNCtGlvl4C8vcZ_GOLg4liy5_NyYEoNczxBlV4SwVlrODt49eQY_JIZlWDxXcgDLjGz3ch7u-HoLGLt0qO7FWhQStscLI-Ieh96u7jfBlGE8OWoWINAaOrIBNANVzoYZVHMTjAMoDPb2dx_91r2fMb-QwcVzQNQfFxsn_CoMUq6VKhgkt3YJy_U86tMd4zc6uyFR70x7Wu09T_9v86LOkNAZw6w6NwhBfNlCzxadCpbsm1qVetbCWF7-z_BjqrFyWsDeqdKAK9hJPWTooySxeF1b4D6t3IeqnLFRCSeBjx0rYPuRgF5ZeSQFDbndDcOCKIIjLdYGwbcb6tZrr-HWhLTt94jy4f1E0ubh62z3rk46z_QBVwBOeLOmEt3AEhxUXwnr3xF3SBsjeaNbCumnXeBtarDCD4-f9M1vw8pZfIk9aYrbztaSc-XWFzZ2DzMfuM9rAYPutdjFs0TzTCcNCVki81F0e3v5nR7Tfg6=w1921-h539-no?authuser=0">


<h1>BITWALLS SPAM MAIL DETECTOR</h1>

<p>The term spam refers to any form of unwanted, unsolicited digital communication that is sent in large quantities. 
Most spam is sent via email, but it can also be distributed by phone calls, text messages, or social media. In last few
years there have been so many attacks and problems related to spams. One of the main reasons to this is the lack of 
tools to scan spam emails and the lack of knowledge related to spams and information technology.</p>


<button class="button button1 center"><a href="https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_button_test">
Spam Detector</a></button>

<button class="button button3 center3"><a href="https://pasindubandaraa.github.io/Quiz-app/">
Quiz</a></button>

</body>""", unsafe_allow_html=True)
