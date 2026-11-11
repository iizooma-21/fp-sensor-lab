"""Theory page: optical sensor theory — WGM, FBG, Fabry-Perot, SPR, plus Assumptions and References."""
import streamlit as st

from core import branding

st.markdown(branding.header_html("Theory — Optical Sensors",
                                 "The sensor-technology science behind the Fabry-Perot interferometer and "
                                 "related optical sensors — use it to justify the models in your report."),
            unsafe_allow_html=True)

tabs = st.tabs(["Optical: WGM", "Optical: FBG / Fabry-Perot / SPR", "Assumptions", "References"])

# ---------------------------------------------------------------------------
with tabs[0]:
    st.subheader("Whispering-gallery-mode (WGM) resonators")
    st.markdown("Light circulating along the rim of a microsphere, microtoroid, microring or microbubble resonates when an integer number "
                "of wavelengths fits the optical path:")
    st.latex(r"2\pi R\,n_{eff}=m\lambda\;\;\Rightarrow\;\;\lambda_m=\frac{2\pi R\,n_{eff}}{m},\qquad \mathrm{FSR}\approx\frac{\lambda^2}{2\pi R\,n_g}")
    st.markdown("The evanescent tail of the mode samples the surrounding analyte. A change of its refractive index $n_s$ shifts the resonance; "
                "$\\eta$ is the fraction of the mode energy in the analyte:")
    st.latex(r"\frac{\Delta\lambda}{\lambda}=\frac{\eta\,\Delta n_s}{n_{eff}}\;\;\Rightarrow\;\; S=\frac{d\lambda}{dn_s}=\frac{\lambda\,\eta}{n_{eff}}\ \ [\text{nm/RIU}]")
    st.markdown(r"For microspheres and microtoroids the app estimates $\eta\approx(\lambda/2\pi R n)^{2/3}$ (a scaling law, valid for $R\gg\lambda$); for rings and microbubbles $\eta$ "
                "is a design input (waveguide geometry / wall thickness).")
    st.markdown("**Linewidth and detection limit.** The loaded quality factor gives the linewidth $\\Gamma=\\lambda/Q$. Fitting a Lorentzian of depth $A$ "
                "sampled with $N_\\Gamma$ points per linewidth at dip-depth-to-noise ratio $\\mathrm{SNR}=A/\\sigma_n$ gives the Cramér-Rao bound for the resonance position:")
    st.latex(r"\sigma_\lambda=\Gamma\sqrt{\frac{2}{\pi N_\Gamma}}\,\frac{1}{\mathrm{SNR}},\qquad \mathrm{LOD}=\frac{3\sigma_\lambda}{S}")
    st.markdown("**Temperature cross-sensitivity** (the main practical problem): thermo-optic effect + thermal expansion + the thermo-optic coefficient of water ($-10^{-4}$/K):")
    st.latex(r"\frac{d\lambda}{dT}=\lambda\left[\alpha+\frac{1}{n_{eff}}\frac{dn}{dT}+\frac{\eta}{n_{eff}}\frac{dn_{water}}{dT}\right]")
    st.markdown("Silica gives $\\approx 14$ pm/K at 1550 nm, silicon $\\approx 90$ pm/K; a 10 mK fluctuation is therefore comparable to a $10^{-5}$ RIU signal.")

# ---------------------------------------------------------------------------
with tabs[1]:
    st.subheader("Fibre Bragg grating (FBG)")
    st.latex(r"\lambda_B=2n_{eff}\Lambda,\qquad \frac{\Delta\lambda_B}{\lambda_B}=(1-p_e)\,k_t\,\varepsilon+(\alpha+\xi)\,\Delta T,\qquad p_e=\frac{n^2}{2}\big[p_{12}-\nu(p_{11}+p_{12})\big]")
    st.markdown("With $p_e\\approx0.22$ this gives about $1.2$ pm/$\\mu\\varepsilon$ and $13$ pm/K at 1550 nm; $k_t$ is the strain-transfer efficiency of the bond. "
                "A temperature error of 1 K is therefore read as roughly $11\\,\\mu\\varepsilon$ (cross-sensitivity). Reflection linewidth of a uniform grating of length $L_g$ and index modulation $\\delta n$:")
    st.latex(r"\Delta\lambda_{FWHM}\approx\lambda_B\sqrt{\left(\frac{\delta n}{2n_{eff}}\right)^2+\left(\frac{\Lambda}{L_g}\right)^2}")
    st.subheader("Extrinsic Fabry-Perot interferometer (EFPI) pressure sensor")
    st.markdown("A fibre end and a thin diaphragm form a cavity of length $L$. Centre deflection of a clamped circular diaphragm (radius $r$, thickness $h$), "
                "phase change and the interferometric output near quadrature:")
    st.latex(r"w_0=\frac{3(1-\nu^2)P\,r^4}{16\,E\,h^3},\qquad \Delta\varphi=\frac{4\pi w_0}{\lambda},\qquad I=I_0\big[1+V\sin(\varphi_b+\Delta\varphi)\big]")
    st.markdown("Fringe visibility drops with cavity length because of the Gaussian-beam divergence "
                r"($V=V_0/\sqrt{1+(2L\lambda/\pi w_m^2)^2}$, $w_m\approx5.2\,\mu$m). The maximum slope is at quadrature. "
                "A **sealed** cavity contains trapped gas that expands with temperature, giving an error $\\Delta P\\approx P_{atm}\\Delta T/T\\approx0.34$ kPa/K. "
                "Noise: shot noise $\\sqrt{2qI}$, transimpedance thermal noise $\\sqrt{4k_BT/R_f}$ and laser relative-intensity noise. "
                r"Diaphragm resonance: $f_1=\dfrac{10.21}{2\pi r^2}\sqrt{D/(\rho h)}$.")
    st.subheader("Surface plasmon resonance (Kretschmann configuration)")
    st.markdown("A TM-polarised beam in a prism excites a surface plasmon on a thin metal film when the in-plane wave-vector of the incident light matches that of the plasmon:")
    st.latex(r"k_x=\frac{2\pi}{\lambda}n_p\sin\theta=\mathrm{Re}\,k_{sp},\qquad k_{sp}=\frac{2\pi}{\lambda}\sqrt{\frac{\varepsilon_m n_s^2}{\varepsilon_m+n_s^2}}")
    st.markdown("The app computes the full three-layer (prism / metal / analyte) Fresnel reflectance and finds the reflectance minimum:")
    st.latex(r"R(\theta)=\left|\frac{r_{01}+r_{12}e^{2ik_{z1}d}}{1+r_{01}r_{12}e^{2ik_{z1}d}}\right|^2,\qquad r_{ij}=\frac{k_{zi}/\varepsilon_i-k_{zj}/\varepsilon_j}{k_{zi}/\varepsilon_i+k_{zj}/\varepsilon_j}")
    st.latex(r"S=\frac{d\theta_{SPR}}{dn_s}\ [\text{deg/RIU}],\qquad \mathrm{FoM}=\frac{S}{\Delta\theta_{FWHM}}")
    st.markdown("Metal permittivities at 633 nm are taken from Johnson & Christy (gold $n=0.18+3.40i$, silver $n=0.06+4.27i$). Angle noise uses the same "
                "Cramér-Rao expression as the WGM with the dip depth included.")

# ---------------------------------------------------------------------------
with tabs[2]:
    st.subheader("Assumptions and limits of the models")
    st.markdown(
        "- All models are **analytical, first-order models** for teaching and design exploration. They capture the dominant physics and its trade-offs, not every second-order effect.\n"
        "- Material constants are typical literature values. The temperature coefficients of silicon piezoresistance versus doping are **digitised trends** "
        "(after Kanda 1982) and the temperature coefficients of $d$ for piezo-ceramics are indicative; enter datasheet values with the *Custom* material for your own device.\n"
        "- The diaphragm formulas assume small deflection (plate theory); the app warns above $w_0/h=0.5$. The membrane-stiffening factor is a simplified correction.\n"
        "- The **evanescent fraction** of microspheres/microtoroids uses a scaling law; for a specific resonator compute $\\eta$ from the mode profile or use the manual value.\n"
        "- The spectral read-out noise uses the Cramér-Rao bound of a Lorentzian line shape (also used for the FBG as an approximation). Real interrogators add laser, thermal and mechanical noise.\n"
        "- SPR uses a fixed wavelength of 633 nm and bulk refractive-index sensing; the temperature effect enters through the water thermo-optic coefficient only.\n"
        "- The virtual experiment treats reading noise as Gaussian and independent. Real data may show drift, colored noise and non-Gaussian outliers.\n"
        "- The machine-learning models learn from what the simulator generates; they are a way to study the learning workflow and surrogate modelling, and they reproduce the physics "
        "they were trained on rather than discover unknown physics. With real measurements the same pages apply unchanged."
    )

# ---------------------------------------------------------------------------
with tabs[3]:
    st.subheader("References")
    st.markdown(
        "1. J. Fraden, *Handbook of Modern Sensors: Physics, Designs, and Applications*, Springer.\n"
        "2. S. P. Timoshenko and S. Woinowsky-Krieger, *Theory of Plates and Shells*, McGraw-Hill (clamped plate stresses and deflections).\n"
        "3. K. J. Vahala, \"Optical microcavities\", *Nature* **424**, 839 (2003).\n"
        "4. F. Vollmer and S. Arnold, \"Whispering-gallery-mode biosensing: label-free detection down to single molecules\", *Nature Methods* **5**, 591 (2008).\n"
        "5. A. Othonos and K. Kalli, *Fiber Bragg Gratings: Fundamentals and Applications*, Artech House; K. O. Hill and G. Meltz, *J. Lightwave Technol.* **15**, 1263 (1997).\n"
        "6. J. Homola, \"Surface plasmon resonance sensors for detection of chemical and biological species\", *Chem. Rev.* **108**, 462 (2008).\n"
        "7. P. B. Johnson and R. W. Christy, \"Optical constants of the noble metals\", *Phys. Rev. B* **6**, 4370 (1972).\n"
        "8. S. M. Kay, *Fundamentals of Statistical Signal Processing, Vol. I: Estimation Theory*, Prentice Hall (Cramér-Rao bound).\n"
        "9. ICH Harmonised Guideline Q2(R1), *Validation of Analytical Procedures* (limit of detection / quantification).\n"
        "10. JCGM 100:2008 (GUM), *Evaluation of measurement data - Guide to the expression of uncertainty in measurement*."
    )
    st.caption("Please check page numbers and editions against the original sources before citing them in your thesis.")
