"""
================================================================================
BIDC Universal Physics Core - Version 4.0 (Phase Transition & Dynamic Capacity)
================================================================================
Copyright (c) 2026 Chan Kai Sin (陳啟先). All Rights Reserved.

Theological & Physical Framework:
    Bidirectional Inter-dimensional Information Distillation Cosmology (BIDC)
    
Core Axiom:
    "Light speed is dynamic across dimensions and serves as the balancing key.
    Overload triggers up-dimensioning; lagging triggers down-dimensioning."

License: MIT License
================================================================================
"""
import numpy as np
import matplotlib.pyplot as plt

def calculate_bidc_hubble_parameter(z, H_base, alpha, beta):
    theta = np.sqrt(1.0 - (alpha / beta)**2)
    chi = beta / alpha
    H_z = H_base * (1.0 + chi * np.tanh(theta * z) * (1.0 + z)**(alpha/beta - 0.25))
    return H_z

def run_real_data_validation():
    print("==================================================================")
    print(" [BIDC Core v4.0] 啟動真實天文觀測數據庫 (CC Dataset) 終極壓力測試")
    print("==================================================================")
    
    ALPHA = 0.72
    BETA = 1.18
    H_BASE = 67.4
    
    cc_dataset = np.array([
        [0.070, 69.0,  19.6], [0.090, 69.0,  12.0], [0.120, 68.6,  26.2],
        [0.170, 83.0,  8.0],  [0.179, 75.0,  4.0],  [0.199, 75.0,  5.0],
        [0.200, 72.9,  29.6], [0.270, 77.0,  14.0], [0.280, 88.8,  36.6],
        [0.352, 83.0,  14.0], [0.380, 83.0,  13.5], [0.400, 95.0,  17.0],
        [0.400, 77.0,  10.2], [0.440, 82.6,  7.8],  [0.478, 80.9,  9.0],
        [0.480, 97.0,  62.0], [0.593, 104.0, 13.0], [0.680, 92.0,  8.0],
        [0.781, 105.0, 12.0], [0.875, 125.0, 17.0], [0.880, 90.0,  40.0],
        [0.900, 117.0, 23.0], [1.037, 154.0, 20.0], [1.300, 168.0, 17.0],
        [1.363, 160.0, 33.6], [1.430, 177.0, 18.0], [1.530, 140.0, 14.0],
        [1.750, 202.0, 40.0], [1.965, 186.5, 50.4], [2.340, 222.0, 7.0],
        [2.360, 226.0, 8.0]
    ])
    
    z_obs = cc_dataset[:, 0]
    H_obs = cc_dataset[:, 1]
    err_obs = cc_dataset[:, 2]
    
    H_pred = calculate_bidc_hubble_parameter(z_obs, H_BASE, ALPHA, BETA)
    chi_squared = np.sum(((H_obs - H_pred) / err_obs) ** 2)
    reduced_chi_squared = chi_squared / len(z_obs)
    
    print(f" [+] 成功導入並比對 {len(z_obs)} 個真實深空宇宙觀測樣本。")
    print(f" [+] BIDC V4 模型減縮卡方值 (Reduced Chi-Squared): {reduced_chi_squared:.4f}")
    print("==================================================================\n")
    
    z_space = np.linspace(0, 2.5, 1000)
    H_curve = calculate_bidc_hubble_parameter(z_space, H_BASE, ALPHA, BETA)
    
    plt.figure(figsize=(11, 6.5))
    plt.errorbar(z_obs, H_obs, yerr=err_obs, fmt='o', color='crimson', alpha=0.7, label='Real Cosmic Surveys Data (CC Dataset)')
    plt.plot(z_space, H_curve, '-', color='orangered', lw=3.5, label='BIDC V4 Model')
    plt.xlabel('Redshift z')
    plt.ylabel('H(z)')
    plt.title('BIDC V4 Validation')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.savefig('bidc_v4_validation_result.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    run_real_data_validation()
