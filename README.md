# African Computer Vision Survey
[Paper](https://arxiv.org/abs/2401.11617)

* ToDos:
- [ ] Cleaning up Code
- [ ] Add refined set data collection code

* Note our work is based on community involvement, be patient with students, postdocs and faculty that are volunteering parts of their times to build this repository.

## Work Phases
* Search queries generation
* Data collection for the three sets: full, refined, and toptier set, in addition to the authors metadata for the refined and toptier set.
* Verification of the refined set based on the authors and topics.
* Classification of the publications abstracts to dataset or not dataset paper, in addition to the manual classification of each dataset.
* Analysis of the data that can be used to reproduce the plots in the paper

## Summary of results
* Top-tier publications per continent - Numbers of researcher-publication pairs for around 45K publications (CVPR, ICCV, ECCV, MICCAI, Neurips, ICLR, ICML, IJCV, TPAMI)


|                     | North America | South America | Africa | Asia  | Europe | Oceania | Total Per Year |
|---------------------|---------------|---------------|--------|-------|--------|---------|----------------|
| 2022                | 7498          | 40            | 21     | 14853 | 4892   | 1024    | 28328          |
| 2021                | 9926          | 83            | 9      | 11948 | 6060   | 803     | 28829          |
| 2020                | 11073         | 69            | 38     | 10431 | 5962   | 796     | 28369          |
| 2019                | 9120          | 32            | 8      | 7622  | 4860   | 611     | 22253          |
| 2018                | 8620          | 48            | 11     | 4925  | 4318   | 491     | 18413          |
| 2017                | 6058          | 21            | 3      | 3205  | 3319   | 378     | 12984          |
| 2016                | 4487          | 21            | 5      | 2276  | 2432   | 299     | 9520           |
| 2015                | 3813          | 39            | 2      | 2183  | 2358   | 284     | 8679           |
| 2014                | 3486          | 21            | 9      | 1585  | 2006   | 260     | 7367           |
| 2013                | 3461          | 27            | 2      | 1713  | 2297   | 267     | 7767           |
| 2012                | 3030          | 13            | 7      | 1402  | 2095   | 164     | 6711           |
| Total per continent | 70572         | 414           | 115    | 62143 | 40599  | 5377    | 179220         |

  
* Top-tier publications per continent - Percentages of researcher publication pairs.


|                     | Africa             | South America     | North America & Asia| Oceania             | Europe             |
|---------------------|--------------------|-------------------|---------------------|---------------------|--------------------|
| 2022                | 0.0741316012425868 | 0.14120304998588  | 78.9007342558599    | 3.61479807963852    | 17.2691330132731   |
| 2021                | 0.0312185646397725 | 0.28790454056679  | 75.8749869922647    | 2.78538971174859    | 21.0205001907801   |
| 2020                | 0.133949028869541  | 0.243223236631534 | 75.8010504423843    | 2.80587965737248    | 21.0158976347421   |
| 2019                | 0.0359502089605896 | 0.143800835842358 | 75.2347998022739    | 2.74569720936503    | 21.8397519435582   |
| 2018                | 0.0597404008037799 | 0.260685385325585 | 73.5621571715636    | 2.66659425405963    | 23.4508227882474   |
| 2017                | 0.0231053604436229 | 0.16173752310536  | 71.341651263093     | 2.91127541589649    | 25.5622304374615   |
| 2016                | 0.0525210084033613 | 0.220588235294118 | 71.0399159663866    | 3.14075630252101    | 25.546218487395    |
| 2015                | 0.0230441295080078 | 0.449360525406153 | 69.0863002650075    | 3.27226639013711    | 27.1690286899412   |
| 2014                | 0.122166417809149  | 0.285054974888014 | 68.8339894122438    | 3.52925207004208    | 27.229537125017    |
| 2013                | 0.0257499678125402 | 0.347624565469293 | 66.6151667310416    | 3.43762070297412    | 29.5738380327025   |
| 2012                | 0.104306362688124  | 0.193711816420802 | 66.0408284905379    | 2.44374906869319    | 31.21740426166     |
| Total per continent | 0.0641669456533869 | 0.231001004352193 | 74.0514451512108    | 3.00022318937619    | 22.6531637094074   |
  
* African publications per region - Number of Publications from the refined set. While refined set has 12155 publications only, few publications were counted twice if belongs to two regions & 2023 publications were ignored.

|                  | Northern Region    | Southern Region    | Western Region | Eastern Region | Central Region    | Total per Year |
|------------------|--------------------|--------------------|----------------|----------------|-------------------|----------------|
| 2022             | 1379               | 188                | 173            | 221            | 17                | 1978           |
| 2021             | 1212               | 185                | 121            | 122            | 23                | 1663           |
| 2020             | 1057               | 179                | 91             | 67             | 16                | 1410           |
| 2019             | 907                | 161                | 73             | 53             | 11                | 1205           |
| 2018             | 808                | 111                | 40             | 40             | 9                 | 1008           |
| 2017             | 655                | 90                 | 27             | 24             | 1                 | 797            |
| 2016             | 626                | 59                 | 21             | 16             | 2                 | 724            |
| 2015             | 421                | 61                 | 10             | 25             | 3                 | 520            |
| 2014             | 429                | 49                 | 19             | 13             | 3                 | 513            |
| 2013             | 310                | 53                 | 6              | 6              | 5                 | 380            |
| 2012             | 300                | 39                 | 13             | 7              | 1                 | 360            |
| Before 2012      | 1298               | 337                | 39             | 50             | 24                | 1748           |
| Total per region | 9402               | 1512               | 633            | 644            | 115               | 12306          |
  
## Verification Phase - Rejected Examples
* Authorship issues:
    * Typo in the country Swaziland instead of Switzerland:
        * Jin, B., Ortiz Segovia, M. V., & Susstrunk, S. (2017). Webly supervised semantic seg- mentation. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 3626–3635.
    * Identifying Papua New Guinea as African country conflating it with Guinea:
        * Sirohi, A., Malik, A., Isha, & Luhach, A. K. (2021). A review on various deep learning techniques for identification of plant diseases. Communications in Computer and Information Science, 1393, 487 – 498. Cited by: 1.
        * Khamparia, A., Singh, A., Luhach, A. K., Pandey, B., & Pandey, D. K. (2020). Classifica- tion and identification of primitive kharif crops using supervised deep convolutional networks. Sustainable Computing: Informatics and Systems, 28, 100340.
        * Doaemo, W., Mohan, M., Adrah, E., Srinivasan, S., & Dalla Corte, A. P. (2020). Exploring forest change spatial patterns in papua new guinea: A pilot study in the bumbu river basin. Land, 9(9), 282.
* Topics relevance issues:
    * Abstract containing keyword for image but the work has no relevance to Computer Vision or images:
        * McCoy, J. T., Kroon, S., & Auret, L. (2018). Variational autoencoders for missing data im- putation with application to a simulated milling circuit. IFAC-PapersOnLine, 51 (21), 141 – 146. Cited by: 42; All Open Access, Bronze Open Access.
          
## References

Please cite our paper if you find it useful in your research

```
@article{omotayo2024survey,
  title={The State of Computer Vision Research in Africa},
  author={Omotayo, Abdul-Hakeem and Mbilinyi, Ashery and Ismaila, Lukman and Turki, Houcemeddine and Abdien, Mahmoud and Gamal, Karim and Tondji, Idriss and Pimi, Yvan and Etori, Naome A and Matar, Marwa M and others and Mennatullah S},
  journal={Journal of AI Research, Fairness and Bias in AI special issue},
  year={2024}
}
```
