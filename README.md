# Global_Science_Academies

The Global Science Academies collection is a dataset of science academies around the world. The data are available in both CSV and JSON formats.
This repository provides both the data and the code of the submitted paper, entitled ["A Dataset for Understanding the Organizational Personality of Global Science Academies"](https://github.com/carriechen/Global_Science_Academies). 

The workflow of the data collecting processed is shown in the Figure 1.

![Figure 1 Data processing workflow](https://github.com/carriechen/Global_Science_Academies/blob/main/images/workflow.png)

[//]: <![Figure 1 Data processing workflow](https://anonymous.4open.science/r/Global_Science_Academies-7B16/images/workflow.png)>



## The data

The schema of the data is described in Figure 2

![Figure 2 Data schema](https://github.com/carriechen/Global_Science_Academies/blob/main/images/schema.png)

[//]: <![Figure 2 Data schema](https://anonymous.4open.science/r/Global_Science_Academies-7B16/images/schema.png)>

```
.
├── data
│   ├── science_academies.csv
│   └── science_academies.json
├── navigation_menu
│   ├── academianacionaldemedicina.org.json
│   ├── academie-sciences.bj.json
│   ├── academiesciencesmoralesetpolitiques.fr.json
│   ...
└── sitemaps
    ├── sitemap_abc.xml
    ├── sitemap_aal.xml
    ├── sitemap_amacad.xml
    ...
```
## The code

### Wikipedia

```python
import wikipedia

>>> wikipedia.search("Polish Academy of Sciences")
```

### Navigation menu

The implemention of webmenu ```webmenu.py```,  use anchor tags like “#nav”, and “#menu” to find the navigation menu content.

### Sitemap

The sitemap of each science academy is implemented by using the Python package [python-sitemap](https://github.com/c4software/python-sitemap).

```bash
python main.py --domain http://akad.gov.al/ash/ --output sitemap_akad.xml -n 4  --debug
```
## Data usage
The global science academies dataset is intended to inspire the use of studies on the organizational behavior of science academies, promote studies on how to bridge the gap between different science academies, and how science academies can play an even greater role in national development and international cooperation. 

The full dataset is temporarily hosted on Anonymous Github. The data will be uploaded to common data sharing platforms and updated regularly, and is available in both CSV and JSON formats. The restricted database has been cross-referenced. It is licensed under CC-BY-SA. The intermediate files and the exhaustive database have not been cross-verified and should not be used directly or at the user's full responsibility.
