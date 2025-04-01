import streamlit as st
import time

def countdown_timer(total_seconds):
    
    placeholder = st.empty()
    
    while total_seconds:
        
        mins, secs = divmod(total_seconds, 60)
        timer_display = f"⏳ {mins:02d}:{secs:02d}"
        placeholder.markdown(f"## {timer_display}")
        time.sleep(1)
        total_seconds -= 1
    placeholder.markdown("## ⏰ Time's up!")
    st.balloons()
    
    
def main():
    
    st.title("⏳ Modern Countdown Timer")
    st.info("Set the timer and press 'Start' to begin the countdown.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        minutes = st.number_input("Minutes", max_value=60, min_value=0, value=0, step=1)
        
    with col2:
        seconds = st.number_input("Seconds", max_value=59, min_value=0, value=0, step=1)
        
    if st.button("Start", use_container_width=True):
        
        total_seconds = minutes * 60 + seconds
        
        if total_seconds > 0:
            countdown_timer(total_seconds)
        else:
            st.error("⛔ Please set a valid timer duration.")
    

if __name__ == '__main__':
    main()
    