# ppack 📦
processing package for my PC..
A lightweight Python package for biosignal preprocessing and utility functions — including filtering, detrending, path management, and more.

---

## 📁 Package Structure
<pre><code> 
ppack/
├── processing/     # signal processing tools
│ ├── init.py
│ ├── detrend.py
│ ├── filter.py
│ ├── CHROM_DEHAAN.py
│ ├── POS_WANG.py
│ └── ICA_POH.py
├── utils/          # File I/O, path handling
│ ├── init.py
│ ├── parameters.py
│ └── flibrary.py
├── init.py
├── README.md
├── LICENSE     # None
└── setup.py    # not yet
 </code></pre>


## 🔗 External Dependencies / Attribution
This package includes or adapts components from the following open-source projects: `rPPG-Toolbox`
<pre><code>
@article{liu2022rppg,
  title={rPPG-Toolbox: Deep Remote PPG Toolbox},
  author={Liu, Xin and Narayanswamy, Girish and ...},
  journal={arXiv preprint arXiv:2210.00716},
  year={2022}
}
</code></pre>
