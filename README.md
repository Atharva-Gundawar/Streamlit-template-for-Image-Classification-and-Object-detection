# Streamlit Template Library for Computer Vision Model Deployment

This repository contains templates for creating files to deploy your Computer Vision models on the web using streamlit and streamlit-webrtc.

## Getting Started

Clone the repository and install the requirements using the following command: 
```
pip install -r requirements.txt
```
Then choose whichever file that suits your project and run the sreamilt server by running:
```
streamlit run <FILE_NAME>
``` 
If you want to increase the default upload size use the following command 
```
streamlit run <FILE_NAME> --server.maxUploadSize=1028 
# maxUploadSize is in mbs
```
----------------------------------------------------------------

## Built With

* [Streamlit](https://streamlit.io/) - The web framework 
* [streamlit-webrtc](https://pypi.org/project/streamlit-webrtc/) - The web framework for Capturing Videos 

## Contributing

Please read [CONTRIBUTING.md](https://github.com/) for details on our code of conduct, and the process for submitting pull requests.


## Authors

* **Atharva Gundawar** - *Initial work* - [Github handle](https://github.com/Atharva-Gundawar)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Object detection Example : https://github.com/robmarkcole/object-detection-app.
* Streamlit Webrtc code snippets : https://github.com/whitphx/streamlit-webrtc-example
