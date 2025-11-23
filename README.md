Please run the following steps in the terminal, one by one, based on the list below.

Setup for window 
1. Create a virtual environment

    python -m venv .venv

2. Activate the virtual environment
    .venv\Scripts\activate.bat

3. Install the required libraries/modules (from requirements.txt) into the virtual environment
    
   pip install -r requirements.txt

4. Start the app using the command - in the root folder (not inside app folder)

   uvicorn app.main:app --reload

Setup for Macbook

1. Create a virtual environment
   
   python -m venv .venv
3. Check uvicon
   
   which uvicon
   
5. Make conda deactivate from current one
   
   conda deactivate
6. make conda activavte for project path (Activate the virtual environment)
   
   source .venv/bin/activate
   
7. Install the required libraries/modules (from requirements.txt) into the virtual environment

   python -m pip install -r requirements.txt
   
8. Start the app using the command - in the root folder (not inside app folder)
   
   python -m uvicorn app.main:app --reload 
