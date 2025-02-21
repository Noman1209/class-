#streamlit
import streamlit as st

st.set_page_config(page_title= "Muhammadnomangrowthmindset project",project_icon="🌟")
st.title("Muhammad Noman Growth Mindset Project Ai project")

st.header("💞 weclcome to your Growth jouney")
. This Ai -powered app helps youbuild a growth mindset by providing you with the tools and resources you need to overcome challenges and achieve your goals. Whether you're looking to improve your skills, build new habits, or develop a positive mindset, this app has everything you need to succeed. Let's get started! 💪🚀")

# quote section 
st.header("💚 To day's Growth Mindst Quote")
st.write(""Success is not final, failure is not fatal: It is the courage to continue that counts." - Winston Churchill")
-
st.header("♡ wahat's Your challenge today?")
user_input = st.text_input("Describe your challenge today", "e.g. I'm struggling to stay focused on my work")


#condition
if user_input:
    st.success(f"💪you're faction:{user_input}.keep pushing forward to word your goal!"💪")
else:
    st.warning("🤔What's your challenge today?")     
    
#reflexing
st.header("🌟Reflect on Your learing")
reflection = st.text_area("Write your reflection here", "e.g. What did you learn today? What challenges did you face? How can you overcome them?")

 if reflection:
    st.success("🌟Great Insight!Your reflection:{reflection}🌟")
 else:
       st.info("🤔Reflecting on past experience help you grow! Share your difficultites") 
       
       
#racheivements
st.header("🏆Celebrate Your Achievements!")
acheievmenr= st.text_inpt ("Share something you' ve achieved today", "e.g. I completed my project ahead of schedule:")


 if achievement:   
    st.success(f"🎉Congratulations!You've achieved:{achievement}🎉")
 else:
     st.info("🤔Big or small,every acheivement counts!Share on now!❤️")
     
     
  #footer   
  st.write("----")
  st.write("👭 keep believing in yourself.Growth is a journey, not a destination. Keep pushing forward and you'll achieve great things!💖")
  st.write("🌟Created with love by Muhammad Noman🌟")
  
     
