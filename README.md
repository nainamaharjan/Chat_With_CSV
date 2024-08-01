The project utilises a fine-tuned language model to answer COVID-19 related questions and generate data visualisations based on user queries.

**Installation Steps**
Clone the Repository:
- git clone https://github.com/nainamaharjan/Chat_With_CSV.git

**To run manually: **
- Install Python if Python is not installed on your machine, download and install it from python.org.
- Install Miniconda Download and install Miniconda from the following link: Miniconda Installation Guide- https://docs.anaconda.com/miniconda/miniconda-install/
- Configure Python Interpreter in Your IDE.
- Go to the project terminal.    
- Install required libraires in the terminal:-  pip install -r requirements.txt
- In the project folder - “settings.py”, you can change the value of “ROWS_TO_ADD” to 10000.
- Open “settings.py” folder  in the project and add the value of the API key. 
    -API_KEY = <your_openAI_API_Key>
- Run the following command in the terminal to start the UI :-  sh start_ui.sh.   Now, the project should be up and the UI should be displayed.
- After the UI is loaded, first click the “Calculate Embeddings” button displayed in the UI. (This will calculate embeddings of the CSV data and store in chromaDB)
- After the “Embeddings Calculated” is shown in UI. You can now ask the queries and get answers.

**To run through docker: **
- Go to the main project directory where the docker file is available.
-  Run the following code in the terminal.
    - docker build --build-arg OPENAI_API_KEY=<your_openAI_API_Key> -t <image_name> --file Dockerfile .
- After completion of running above code. Run this.
    - docker run  -it <image_name> 
- Click the link for streamlit UI displayed in the docker logs. 
- After the UI is loaded,  first click the “Calculate Embeddings” button displayed in the UI. (This will calculate embeddings of the CSV data and store in chromaDB)
- After the “Embeddings Calculated” is shown in UI. You can now ask the queries and get answers. 

