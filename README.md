# African Computer Vision Survey

## Work Phases
* Search queries generation
* Data collection for the three sets: full, refined, and toptier set, in addition to the authors metadata for the refined and toptier set.
* Verification of the refined set based on the authors and topics.
* Classification of the publications abstracts to dataset or not dataset paper, in addition to the data of the manual classification of each dataset.
* Analysis of the data that was used to reproduce the plots in the paper

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

  
* African publications per region.

  
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
