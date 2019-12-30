# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 20:19:29 2019

@author: Lee Sak Park
"""

# ===============================
# Imports
# ===============================


import tkinter as tk
from tkinter import ttk
from scipy.stats import t
from scipy.stats import norm
import numpy as np

# =================================
# OOP Class 
# =================================

class OOP():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("STA296 Calculator")
        self.null_value = "           "
        self.tabs()
        self.win.iconbitmap('C:\\Users\\Lee Sak Park\\Documents\\GitHub\\leepark.github.io\\STA296\\UKY.ico')


# =====================================
# calculate functions
# =====================================

    def calculate_single_mean(self):
        m = self.tab1_tbox1.get()
        sd = self.tab1_tbox2.get()
        n = self.tab1_tbox3.get()
        cl = self.tab1_tbox4.get()/2 + .5
        
        lower = m - t.ppf(q = cl, df = n-1)*sd/(n**.5)
        lower = str(round(lower,4))
        upper = m + t.ppf(q = cl, df = n-1)*sd/(n**.5)
        upper = str(round(upper,4))
        
        self.answer1 = lower + "  ~  " + upper
        
        self.tbox_answer1.configure(text = self.answer1)
        
    def calculate_two_mean(self):
        
        m1 = self.tab1_tbox_sp1_m.get()
        sd1 = self.tab1_tbox_sp1_sd.get()
        n1 = self.tab1_tbox_sp1_n.get()
        
        m2 = self.tab1_tbox_sp2_m.get()
        sd2 = self.tab1_tbox_sp2_sd.get()
        n2 = self.tab1_tbox_sp2_n.get()
        
        cl = self.tab1_tbox_2sp_cl.get()/2 + .5
        
        mean_diff = m1-m2
        se = (sd1**2/n1 + sd2**2/n2)**.5
        d = min([n1, n2])-1
        
        
        lower = mean_diff - t.ppf(q = cl, df =d)*se
        lower = str(round(lower, 4))
        upper = mean_diff + t.ppf(q = cl, df =d)*se
        upper = str(round(upper, 4))
        
        self.answer2 = lower + "  ~  " + upper
        
        self.tbox_answer1.configure(text = self.answer2)
        
    
    def calculate_one_proportion(self):
        
        p_hat = self.tab2_tbox1.get()
        q = 1- p_hat
        n = self.tab2_tbox2.get()
        cl = self.tab2_tbox3.get()/2 + .5
        se = (p_hat * q / n)**.5
        
        lower = p_hat - norm.ppf(q = cl)*se
        lower = str(round(lower, 4))
        upper = p_hat + norm.ppf(q = cl)*se
        upper = str(round(upper, 4))

        self.answer3 = lower + "  ~  " + upper

        self.tbox_answer2.configure(text = self.answer3)

        
        
    def calculate_two_proportion(self):
        
        p_hat1 = self.tab2_tbox_sp1_p.get()
        n1 = self.tab2_tbox_sp1_n.get()
        p_hat2 = self.tab2_tbox_sp2_p.get()
        n2 = self.tab2_tbox_sp2_n.get()
        cl = self.tab2_tbox_sp1_CL.get()/2+.5
        
        diff = p_hat1 - p_hat2
        se = (p_hat1*(1-p_hat1)/n1 + p_hat2*(1-p_hat2)/n2)**.5
        z = norm.ppf(q= cl)
        
        lower = diff - z*se
        lower = str(round(lower, 4))
        upper = diff + z*se
        upper = str(round(upper, 4))
        
        self.answer4 = lower + "  ~  " + upper

        self.tbox_answer2.configure(text = self.answer4)
    
    def one_t_test(self):
        se = self.tab3_single_sd.get()/(self.tab3_single_n.get())**.5
        n = self.tab3_single_n.get()
        mean_h0 = self.tab3_single_H0.get() 
        x_bar = self.tab3_single_mean.get()
        test_type = self.type_of_test
        alpha = self.tab3_single_alpha.get()
        diff = x_bar - mean_h0
        if test_type == "two":
            t_statistic = str(round((x_bar - mean_h0)/se, 4))
            lower = str(round(t.ppf(q = alpha/2, df = n-1),4))
            upper = str(round(t.ppf(q = 1- alpha/2, df = n-1),4))
            rejection_region = lower + "   //   " + upper
            if(diff < 0):
                p_value = t.cdf((x_bar - mean_h0)/se, df = n-1)
                p_value = str(round(p_value*2, 4))
            else:
                p_value = 1- t.cdf((x_bar - mean_h0)/se, df = n-1)
                p_value = str(round(p_value*2, 4))
            self.answer_tab3_answer1.configure(text = t_statistic)
            self.answer_tab3_answer2.configure(text = rejection_region)
            self.answer_tab3_answer3.configure(text = p_value)
        elif test_type == "left":
            t_statistic = str(round((x_bar - mean_h0)/se, 4))
            lower = str(round(t.ppf(q = alpha, df = n-1),4))
            rejection_region = lower
            p_value = t.cdf((x_bar - mean_h0)/se, df = n-1)
            p_value = str(round(p_value, 4))
            self.answer_tab3_answer1.configure(text = t_statistic)
            self.answer_tab3_answer2.configure(text = rejection_region)
            self.answer_tab3_answer3.configure(text = p_value)
        else:
            t_statistic = str(round((x_bar - mean_h0)/se, 4))
            upper = str(round(t.ppf(q = 1-alpha, df = n-1),4))
            rejection_region = upper
            p_value = 1-t.cdf((x_bar - mean_h0)/se, df = n-1)
            p_value = str(round(p_value, 4))
            self.answer_tab3_answer1.configure(text = t_statistic)
            self.answer_tab3_answer2.configure(text = rejection_region)
            self.answer_tab3_answer3.configure(text = p_value)
            
            
    def two_t_test(self):
        sample1_mean = self.tab3_sample1_mean.get()
        sample1_sd = self.tab3_sample1_sd.get()  
        sample1_n = self.tab3_sample1_n.get()
        sample2_mean = self.tab3_sample2_mean.get()
        sample2_sd = self.tab3_sample2_sd.get()  
        sample2_n = self.tab3_sample2_n.get()
        alpha = self.tab3_sample1_alpha.get()
        diff = sample1_mean - sample2_mean
        se = (sample1_sd**2/sample1_n + sample2_sd**2/sample2_n)**.5
        t_statistic = (diff)/se
        test_type = self.type_of_test
        n = min([sample1_n, sample2_n])
        
        if test_type == "two":
            lower = str(round(t.ppf(q = alpha/2, df = n-1),4))
            upper = str(round(t.ppf(q = 1- alpha/2, df = n-1),4))
            rejection_region = lower + "   //   " + upper
            if(t_statistic < 0):
                p_value = t.cdf(t_statistic, df = n-1)
                p_value = str(round(p_value*2, 4))
            else:
                p_value = 1- t.cdf(t_statistic, df = n-1)
                p_value = str(round(p_value*2, 4))
            self.answer_tab3_answer1.configure(text = str(round(t_statistic, 4)))
            self.answer_tab3_answer2.configure(text = rejection_region)
            self.answer_tab3_answer3.configure(text = p_value)
        elif test_type == "left":
            lower = str(round(t.ppf(q = alpha, df = n-1),4))
            rejection_region = lower
            p_value = t.cdf(t_statistic, df = n-1)
            p_value = str(round(p_value, 4))
            self.answer_tab3_answer1.configure(text = str(round(t_statistic, 4)))
            self.answer_tab3_answer2.configure(text = rejection_region)
            self.answer_tab3_answer3.configure(text = p_value)
        else:
            upper = str(round(t.ppf(q = 1-alpha, df = n-1),4))
            rejection_region = upper
            p_value = 1-t.cdf(t_statistic, df = n-1)
            p_value = str(round(p_value, 4))
            self.answer_tab3_answer1.configure(text = str(round(t_statistic, 4)))
            self.answer_tab3_answer2.configure(text = rejection_region)
            self.answer_tab3_answer3.configure(text = p_value)
            
            
    def one_z_test(self):
        p = self.tab4_single_p.get()
        p_hat = self.tab4_single_p_hat.get()
        n = self.tab4_single_n.get()
        alpha = self.tab4_single_alpha.get()
        test_type = self.type_of_test
        se = (p_hat*(1-p_hat)/n)**.5
        diff = p_hat - p
        z_statistic = diff/se
        if test_type == "two":
            lower = str(round(norm.ppf(q = alpha/2),4))
            upper = str(round(norm.ppf(q = 1- alpha/2),4))
            rejection_region = lower + "   //   " + upper
            if z_statistic < 0:
                p_value = norm.cdf(z_statistic)
                p_value = str(round(p_value*2, 4))
            else:
                p_value = 1-norm.cdf(z_statistic)
                p_value = str(round(p_value*2, 4))
        elif test_type == "left":
            lower = str(round(norm.ppf(q = alpha), 4))
            rejection_region = lower
            p_value = norm.cdf(z_statistic)
            p_value = str(round(p_value, 4))
        elif test_type == "right":
            rejection_region = str(round(norm.ppf(q = 1-alpha), 4))
            p_value = 1-norm.cdf(z_statistic)
            p_value = str(round(p_value, 4))
        self.tab4_answer1.configure(text = str(round(z_statistic, 4)))
        self.tab4_answer2.configure(text = rejection_region)
        self.tab4_answer3.configure(text = p_value)
        
        
    
    def two_z_test(self):
        p1 = self.tab4_sample1_p_hat.get()
        p2 = self.tab4_sample2_p_hat.get()
        n1 = self.tab4_sample1_n.get()
        n2 = self.tab4_sample2_n.get()
        alpha = self.tab4_sample1_alpha.get()
        diff = p1-p2
        pooled = (p1*n1+p2*n2)/(n1+n2)
        se = np.sqrt(pooled*(1-pooled))*np.sqrt(1/n1 + 1/n2)
        z_statistic = diff/se
        test_type = self.type_of_test
        
        if test_type == "two":
            lower = str(round(norm.ppf(q = alpha/2),4))
            upper = str(round(norm.ppf(q = 1- alpha/2),4))
            rejection_region = lower + "   //   " + upper
            if z_statistic < 0:
                p_value = norm.cdf(z_statistic)
                p_value = str(round(p_value*2, 4))
            else:
                p_value = 1-norm.cdf(z_statistic)
                p_value = str(round(p_value*2, 4))
        elif test_type == "left":
            lower = str(round(norm.ppf(q = alpha), 4))
            rejection_region = lower
            p_value = norm.cdf(z_statistic)
            p_value = str(round(p_value, 4))
        elif test_type == "right":
            rejection_region = str(round(norm.ppf(q = 1-alpha), 4))
            p_value = 1-norm.cdf(z_statistic)
            p_value = str(round(p_value, 4))
        self.tab4_answer1.configure(text = str(round(z_statistic, 4)))
        self.tab4_answer2.configure(text = rejection_region)
        self.tab4_answer3.configure(text = p_value)
                
                
                
                
                
# ==============================================================================================
# Radiohead button function ====================================================================
# ==============================================================================================

    def radCall(self):
        radSel = self.radVar.get()
        if   radSel == 1: self.type_of_test = "two"
        elif radSel == 2: self.type_of_test = "left"
        elif radSel == 3: self.type_of_test = "right"
            
    def radCall1(self):
        radSel = self.radVar1.get()
        if   radSel == 1: self.type_of_test = "two"
        elif radSel == 2: self.type_of_test = "left"
        elif radSel == 3: self.type_of_test = "right"

            
# ===============================================================================================
# Creating tabs =================================================================================
# ===============================================================================================

        
    def tabs(self):
        
# ===============================================================================================
# Listing tabs ===================================================================================
# ===============================================================================================
        
        
        tabControl = ttk.Notebook(self.win)
        
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text = "CI_mean")
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text = "CI_proportion")
        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text = "t_test for mean")
        tab4 = ttk.Frame(tabControl)
        tabControl.add(tab4, text = "z_test for proportion")
        
        tabControl.pack(expand = 1, fill = "both")
        
        
# ===============================================================================================
# Codes for tab 1 ===============================================================================
# ===============================================================================================
        
        labelframe = ttk.LabelFrame(tab1, text = "Confidence Interval for Single Mean")
        labelframe.grid(column = 0, row = 0, padx = 8, pady = 8)
        tab1_labels_left = ["Sample Mean : ", "Stample Stdev : ", "Sample Size : ", "Confidence Level"]
        for r in range(4):
            ttk.Label(labelframe, 
                      text = tab1_labels_left[r]).grid(column = 0, 
                                                       row = r, 
                                                       sticky = "W")           

        
        self.tab1_tbox1 = tk.DoubleVar()
        self.tab1_tbox1_entered = ttk.Entry(labelframe, width = 12, textvariable = self.tab1_tbox1)
        self.tab1_tbox1_entered.grid(column = 1, row = 0, sticky = "W")
        self.tab1_tbox2 = tk.DoubleVar()
        self.tab1_tbox2_entered = ttk.Entry(labelframe, width = 12, textvariable = self.tab1_tbox2)
        self.tab1_tbox2_entered.grid(column = 1, row = 1, sticky = "W")
        self.tab1_tbox3 = tk.DoubleVar()
        self.tab1_tbox3_entered = ttk.Entry(labelframe, width = 12, textvariable = self.tab1_tbox3)
        self.tab1_tbox3_entered.grid(column = 1, row = 2, sticky = "W")
        self.tab1_tbox4 = tk.DoubleVar()
        self.tab1_tbox4_entered = ttk.Entry(labelframe, width = 12, textvariable = self.tab1_tbox4)
        self.tab1_tbox4_entered.grid(column = 1, row = 3, sticky = "W")
        self.excute1 = ttk.Button(labelframe, text = "Run", command = self.calculate_single_mean)
        self.excute1.grid(column = 1, row = 4, sticky = "W", columnspan = 2)

        labelframe_answer1 = ttk.LabelFrame(tab1, text = "Answer")
        labelframe_answer1.grid(column = 0, row = 2, padx = 8, pady = 8, columnspan = 2)
        tbox_answer1_label = ttk.Label(labelframe_answer1, text = "Confidence Interval: ")
        tbox_answer1_label.grid(column = 0, row = 0, sticky = "W")
        self.tbox_answer1 = ttk.Label(labelframe_answer1, text = self.null_value)
        self.tbox_answer1.grid(column = 1, row = 0, sticky = "W")
        
        
        
        # With the second frame, we have two frames each for each sample        
        labelframe1 = ttk.LabelFrame(tab1, text = "Confidence Interval for Two Means")
        labelframe1.grid(column = 1, row = 0, padx = 8, pady = 8, columnspan = 2, rowspan = 2)
        # Names
        labelframe_names = ttk.LabelFrame(labelframe1)
        labelframe_names.grid(column =0, row = 0, padx = 4, pady = 4)
        # for sample 1
        labelframe_sample1 = ttk.LabelFrame(labelframe1, text = "Sample1")
        labelframe_sample1.grid(column = 1, row = 0, padx = 4, pady = 4)
        # for sample 2
        labelframe_sample2 = ttk.LabelFrame(labelframe1, text = "Sample2")
        labelframe_sample2.grid(column = 2, row = 0, padx = 4, pady = 4)

        #labels
        tab1_labels_right = ["Sample Mean : ", "Stample Stdev : ", "Sample Size : "]
        for r in range(len(tab1_labels_right)):
            ttk.Label(labelframe_names, text = tab1_labels_right[r]).grid(column = 0, row = r, sticky = "W")
        
        # for sample 1
        self.tab1_tbox_sp1_m = tk.DoubleVar()
        self.tab1_tbox_sp1_m_entered = ttk.Entry(labelframe_sample1, width = 12, textvariable = self.tab1_tbox_sp1_m)
        self.tab1_tbox_sp1_m_entered.grid(column = 1, row = 0, sticky = "W")
        self.tab1_tbox_sp1_sd = tk.DoubleVar()
        self.tab1_tbox_sp1_sd_entered = ttk.Entry(labelframe_sample1, width = 12, textvariable = self.tab1_tbox_sp1_sd)
        self.tab1_tbox_sp1_sd_entered.grid(column = 1, row = 1, sticky = "W")
        self.tab1_tbox_sp1_n = tk.DoubleVar()
        self.tab1_tbox_sp1_n_entered = ttk.Entry(labelframe_sample1, width = 12, textvariable = self.tab1_tbox_sp1_n)
        self.tab1_tbox_sp1_n_entered.grid(column = 1, row = 2, sticky = "W")
        self.excute2 = ttk.Button(labelframe1, text = "Run", command = self.calculate_two_mean)
        self.excute2.grid(column = 2, row =2, sticky = "W", columnspan = 2)

        
        # for sample 2
        self.tab1_tbox_sp2_m = tk.DoubleVar()
        self.tab1_tbox_sp2_m_entered = ttk.Entry(labelframe_sample2, width = 12, textvariable = self.tab1_tbox_sp2_m)
        self.tab1_tbox_sp2_m_entered.grid(column = 1, row = 0, sticky = "W")
        self.tab1_tbox_sp2_sd = tk.DoubleVar()
        self.tab1_tbox_sp2_sd_entered = ttk.Entry(labelframe_sample2, width = 12, textvariable = self.tab1_tbox_sp2_sd)
        self.tab1_tbox_sp2_sd_entered.grid(column = 1, row = 1, sticky = "W")
        self.tab1_tbox_sp2_n = tk.DoubleVar()
        self.tab1_tbox_sp2_n_entered = ttk.Entry(labelframe_sample2, width = 12, textvariable = self.tab1_tbox_sp2_n)
        self.tab1_tbox_sp2_n_entered.grid(column = 1, row = 2, sticky = "W")

        
        labelframe2 = ttk.LabelFrame(labelframe1)
        labelframe2.grid(column = 0, row = 1, padx = 5, pady = 10, columnspan = 2)

        
        self.tab1_tbox_2sp_cl = tk.DoubleVar()
        self.tab1_tbox_2sp_cl_entered = ttk.Entry(labelframe2, width = 12, textvariable = self.tab1_tbox_2sp_cl)
        self.tab1_tbox_2sp_cl_entered.grid(column = 1, row = 0, sticky = "W")

        b_label4 = ttk.Label(labelframe2, text = "Confidence Level : ")
        b_label4.grid(column = 0, row = 0, sticky = "W")
        
# =================================================================================================================
# ==  tab2  =======================================================================================================
# =================================================================================================================
        
        
        # Single Proportion
        
        labelframe1_tab2 = ttk.LabelFrame(tab2, text = "Confidence Interval for Single Proportion")
        labelframe1_tab2.grid(column = 0, row = 0, padx = 8, pady = 8)
        tab2_labels_left = ["p_hat : ", "n : ", "Confidence Level : "]
        for r in range(len(tab2_labels_left)):
            ttk.Label(labelframe1_tab2, text = tab2_labels_left[r]).grid(column = 0, row = r, sticky = "W")
        
        
        self.tab2_tbox1 = tk.DoubleVar()
        self.tab2_tbox1_entered = ttk.Entry(labelframe1_tab2, width = 12, textvariable = self.tab2_tbox1)
        self.tab2_tbox1_entered.grid(column = 1, row = 0, sticky = "W")
        self.tab2_tbox2 = tk.DoubleVar()
        self.tab2_tbox2_entered = ttk.Entry(labelframe1_tab2, width = 12, textvariable = self.tab2_tbox2)
        self.tab2_tbox2_entered.grid(column = 1, row = 1, sticky = "W")
        self.tab2_tbox3 = tk.DoubleVar()
        self.tab2_tbox3_entered = ttk.Entry(labelframe1_tab2, width = 12, textvariable = self.tab2_tbox3)
        self.tab2_tbox3_entered.grid(column = 1, row = 2, sticky = "W")
        self.excute3 = ttk.Button(labelframe1_tab2, text = "Run", command = self.calculate_one_proportion)
        self.excute3.grid(column = 1, row =3, sticky = "W", columnspan = 2)

        
        # Two Proportion
        
        ## Big Label Frame containing everything for two samples
        labelframe_big_tab2 = ttk.LabelFrame(tab2, text = "Confidence Interval for Two Proportions")
        labelframe_big_tab2.grid(column = 1, row = 0, padx = 8, pady = 8)
        
        
        # Name Labels
        labelframe_small_tab2_names = ttk.LabelFrame(labelframe_big_tab2, text = "")
        labelframe_small_tab2_names.grid(column = 0, row = 0, padx = 5, pady = 5)
                
        d_label1 = ttk.Label(labelframe_small_tab2_names, text="Sample Proportions : ")
        d_label1.grid(column=0, row=0, sticky='W')
        d_label2 = ttk.Label(labelframe_small_tab2_names, text = "Sample Size : ")
        d_label2.grid(column = 0, row = 1, sticky = "W")
        
        # Confidence Level LF and Label
        
        labelframe_small_tab2_CL = ttk.LabelFrame(labelframe_big_tab2)
        labelframe_small_tab2_CL.grid(column = 0, row = 1, padx = 5, pady = 5, columnspan = 2)

        d_label3 = ttk.Label(labelframe_small_tab2_CL, text = "Confidence Level :           ")
        d_label3.grid(column = 0, row = 0, sticky = "W")
        
        self.tab2_tbox_sp1_CL = tk.DoubleVar()
        self.tab2_tbox_sp1_CL_entered = ttk.Entry(labelframe_small_tab2_CL, width = 12, 
                                                  textvariable = self.tab2_tbox_sp1_CL)
        self.tab2_tbox_sp1_CL_entered.grid(column = 1, row = 0, sticky = "W")

        
        # Run Button
        
        self.excute4 = ttk.Button(labelframe_big_tab2, text = "Run", command = self.calculate_two_proportion)
        self.excute4.grid(column = 2, row =3, sticky = "W", columnspan = 2)

        # Sample 1
        labelframe_small_tab2_sample1 = ttk.LabelFrame(labelframe_big_tab2, text = "Sample 1")
        labelframe_small_tab2_sample1.grid(column = 1, row = 0, padx = 5, pady = 5)
        
        self.tab2_tbox_sp1_p = tk.DoubleVar()
        self.tab2_tbox_sp1_p_entered = ttk.Entry(labelframe_small_tab2_sample1, width = 12, 
                                                 textvariable = self.tab2_tbox_sp1_p)
        self.tab2_tbox_sp1_p_entered.grid(column = 1, row = 0, sticky = "W")
        self.tab2_tbox_sp1_n = tk.DoubleVar()
        self.tab2_tbox_sp1_n_entered = ttk.Entry(labelframe_small_tab2_sample1, width = 12, 
                                                 textvariable = self.tab2_tbox_sp1_n)
        self.tab2_tbox_sp1_n_entered.grid(column = 1, row = 1, sticky = "W")
        
        # Sample 2
        labelframe_small_tab2_sample2 = ttk.LabelFrame(labelframe_big_tab2, text = "Sample 2")
        labelframe_small_tab2_sample2.grid(column = 2, row = 0, padx = 5, pady = 5)
        
        self.tab2_tbox_sp2_p = tk.DoubleVar()
        self.tab2_tbox_sp2_p_entered = ttk.Entry(labelframe_small_tab2_sample2, width = 12, 
                                                 textvariable = self.tab2_tbox_sp2_p)
        self.tab2_tbox_sp2_p_entered.grid(column = 1, row = 0, sticky = "W")
        self.tab2_tbox_sp2_n = tk.DoubleVar()
        self.tab2_tbox_sp2_n_entered = ttk.Entry(labelframe_small_tab2_sample2, width = 12, 
                                                 textvariable = self.tab2_tbox_sp2_n)
        self.tab2_tbox_sp2_n_entered.grid(column = 1, row = 1, sticky = "W")
        
        
        # Answer LableFrame     
        
        labelframe3_tab2 = ttk.LabelFrame(tab2, text = "Result")
        labelframe3_tab2.grid(column = 0, row = 2, padx = 8, pady = 8, columnspan = 2)
        tbox_answer2_label = ttk.Label(labelframe3_tab2, text = "Confidence Interval: ")
        tbox_answer2_label.grid(column = 0, row = 0, sticky = "W")
        self.tbox_answer2 = ttk.Label(labelframe3_tab2, text= self.null_value)
        self.tbox_answer2.grid(column = 1, row = 0, sticky = "W")
        

# =================================================================================================================
# ==  tab3: t test for mean(s)  ===================================================================================
# =================================================================================================================
        # Frame0 : Radiohead buttons for types of test ============================================================
        # =========================================================================================================
        labelframe0_tab3 = ttk.LabelFrame(tab3, text = "Types of Test")
        labelframe0_tab3.grid(column = 0, row = 0, padx = 8, pady = 8, columnspan = 3)

        
        self.radVar = tk.IntVar()

        rad1 = tk.Radiobutton(labelframe0_tab3, text = "two_way" , variable=self.radVar, value=1, command=self.radCall)
        rad1.grid(column=0, row=0, sticky=tk.W)   

        rad2 = tk.Radiobutton(labelframe0_tab3, text = "left (Mean 1 < Mean 2)", variable=self.radVar, value=2, command=self.radCall)
        rad2.grid(column=1, row=0, sticky=tk.W)  

        rad3 = tk.Radiobutton(labelframe0_tab3,  text = "right (Mean 1 > Mean 2)", variable=self.radVar, value=3, command=self.radCall)
        rad3.grid(column=2, row=0, sticky=tk.W)

    
    
    
    
    
        # Frame1: Single Mean =====================================================================================
        # =========================================================================================================
        
        labelframe1_tab3 = ttk.LabelFrame(tab3, text = "Test for Single Mean")
        labelframe1_tab3.grid(column = 0, row = 1, padx = 8, pady = 8)
        
        tab3_labels_left = ["Mean from H_0 : ","Sample Mean : ","Sample stdev : ", "Sample Size : ","Alpha : "]
        for r in range(len(tab3_labels_left)):
            ttk.Label(labelframe1_tab3, text = tab3_labels_left[r]).grid(column = 0, row = r, sticky = "W")
            

        self.tab3_single_H0 = tk.DoubleVar()
        self.tab3_single_H0_entered = ttk.Entry(labelframe1_tab3, width = 12, textvariable = self.tab3_single_H0)
        self.tab3_single_H0_entered.grid(column = 1, row = 0, sticky = "W")

        self.tab3_single_mean = tk.DoubleVar()
        self.tab3_single_mean_entered = ttk.Entry(labelframe1_tab3, width = 12, textvariable = self.tab3_single_mean)
        self.tab3_single_mean_entered.grid(column = 1, row = 1, sticky = "W")
        
        self.tab3_single_sd = tk.DoubleVar()
        self.tab3_single_sd_entered = ttk.Entry(labelframe1_tab3, width = 12, textvariable = self.tab3_single_sd)
        self.tab3_single_sd_entered.grid(column = 1, row = 2, sticky = "W")
        
        self.tab3_single_n = tk.DoubleVar()
        self.tab3_single_n_entered = ttk.Entry(labelframe1_tab3, width = 12, textvariable = self.tab3_single_n)
        self.tab3_single_n_entered.grid(column = 1, row = 3, sticky = "W")
        
        self.tab3_single_alpha = tk.DoubleVar()
        self.tab3_single_alpha_entered = ttk.Entry(labelframe1_tab3, width = 12, textvariable = self.tab3_single_alpha)
        self.tab3_single_alpha_entered.grid(column = 1, row = 4, sticky = "W")
        
        self.excute5 = ttk.Button(labelframe1_tab3, text = "Run", command = self.one_t_test)
        self.excute5.grid(column = 1, row = 5, sticky = "E", columnspan = 2)

        
        
        # Frame2: Two Means =======================================================================================
        # =========================================================================================================

        labelframe2_tab3 = ttk.LabelFrame(tab3, text = "Test for Difference in Means")
        labelframe2_tab3.grid(column = 1, row = 1, padx = 8, pady = 8, columnspan = 2, rowspan = 2)
        
        # Names
        labelframe2_tab3_names = ttk.LabelFrame(labelframe2_tab3)
        labelframe2_tab3_names.grid(column =0, row = 0, padx = 4, pady = 4)
        # for sample 1
        labelframe2_tab3_sample1 = ttk.LabelFrame(labelframe2_tab3, text = "Sample 1")
        labelframe2_tab3_sample1.grid(column = 1, row = 0, padx = 4, pady = 4)
        # for sample 2
        labelframe2_tab3_sample2 = ttk.LabelFrame(labelframe2_tab3, text = "Sample 2")
        labelframe2_tab3_sample2.grid(column = 2, row = 0, padx = 4, pady = 4)
        # for alpha
        labelframe2_tab3_alpha = ttk.LabelFrame(labelframe2_tab3, text = "Sample 2")
        labelframe2_tab3_alpha.grid(column = 0, row = 1, padx = 4, pady = 1, columnspan = 2)

        #labels
        b_label1 = ttk.Label(labelframe2_tab3_names, text="Sample Mean : ")
        b_label1.grid(column=0, row=0, sticky='W')
        b_label2 = ttk.Label(labelframe2_tab3_names, text = "Sample stdev : ")
        b_label2.grid(column = 0, row = 1, sticky = "W")
        b_label3 = ttk.Label(labelframe2_tab3_names, text = "Sample Size : ")
        b_label3.grid(column = 0, row = 2, sticky = "W")

        
        # for sample 1
        self.tab3_sample1_mean = tk.DoubleVar()
        self.tab3_sample1_mean_entered = ttk.Entry(labelframe2_tab3_sample1, width = 12, 
                                                   textvariable = self.tab3_sample1_mean)
        self.tab3_sample1_mean_entered.grid(column = 0, row = 0, sticky = "W")
        self.tab3_sample1_sd = tk.DoubleVar()
        self.tab3_sample1_sd_entered = ttk.Entry(labelframe2_tab3_sample1, width = 12, 
                                                 textvariable = self.tab3_sample1_sd)
        self.tab3_sample1_sd_entered.grid(column = 0, row = 1, sticky = "W")
        self.tab3_sample1_n = tk.DoubleVar()
        self.tab3_sample1_n_entered = ttk.Entry(labelframe2_tab3_sample1, width = 12, 
                                                textvariable =self.tab3_sample1_n)
        self.tab3_sample1_n_entered.grid(column = 0, row = 2, sticky = "W")
        
        # for sample 2

        self.tab3_sample2_mean = tk.DoubleVar()
        self.tab3_sample2_mean_entered = ttk.Entry(labelframe2_tab3_sample2, width = 12, 
                                                   textvariable = self.tab3_sample2_mean)
        self.tab3_sample2_mean_entered.grid(column = 0, row = 0, sticky = "W")
        self.tab3_sample2_sd = tk.DoubleVar()
        self.tab3_sample2_sd_entered = ttk.Entry(labelframe2_tab3_sample2, width = 12, 
                                                 textvariable = self.tab3_sample2_sd)
        self.tab3_sample2_sd_entered.grid(column = 0, row = 1, sticky = "W")
        self.tab3_sample2_n = tk.DoubleVar()
        self.tab3_sample2_n_entered = ttk.Entry(labelframe2_tab3_sample2, width = 12, 
                                                textvariable =self.tab3_sample2_n)
        self.tab3_sample2_n_entered.grid(column = 0, row = 2, sticky = "W")
        
        # for alpha
        b_label4 = ttk.Label(labelframe2_tab3_alpha, text = "Alpha :                  ")
        b_label4.grid(column = 0, row = 0, sticky = "W")

        self.tab3_sample1_alpha = tk.DoubleVar()
        self.tab3_sample1_alpha_entered = ttk.Entry(labelframe2_tab3_alpha, width = 12, 
                                                    textvariable =self.tab3_sample1_alpha)
        self.tab3_sample1_alpha_entered.grid(column = 1, row = 0, sticky = "W")

        # run button
        self.excute5 = ttk.Button(labelframe2_tab3, text = "Run", command = self.two_t_test)
        self.excute5.grid(column = 2, row = 4 , sticky = "E")
        
        
        # =======================================
        # Answer ================================
        # =======================================
        
        labelframe2_tab3_answer = ttk.LabelFrame(tab3, text = "Answer")
        labelframe2_tab3_answer.grid(column = 0, row = 3, padx = 4, pady = 1, columnspan = 3)
        answer_tab3_names = ["t-test statistics : ", "rejection regions : ", "p-value : "]
        for r in range(len(answer_tab3_names)):
            ttk.Label(labelframe2_tab3_answer, text = answer_tab3_names[r]).grid(column = 0, row = r, sticky = "W")

        self.answer_tab3_answer1 = ttk.Label(labelframe2_tab3_answer, text = "")
        self.answer_tab3_answer1.grid(column = 1, row = 0)
        self.answer_tab3_answer2 = ttk.Label(labelframe2_tab3_answer, text = "")
        self.answer_tab3_answer2.grid(column = 1, row = 1)
        self.answer_tab3_answer3= ttk.Label(labelframe2_tab3_answer, text = "")
        self.answer_tab3_answer3.grid(column = 1, row = 2)
        
        
        
        tbox_answer2_label = ttk.Label(labelframe3_tab2, text = "Confidence Interval: ")
        tbox_answer2_label.grid(column = 0, row = 0, sticky = "W")
        self.tbox_answer2 = ttk.Label(labelframe3_tab2, text= self.null_value)
        self.tbox_answer2.grid(column = 1, row = 0, sticky = "W")

        
        
# =================================================================================================================
# ==  tab4: z test for proportion(s)  ===================================================================================
# =================================================================================================================
        # Frame0 : Radiohead buttons for types of test ============================================================
        # =========================================================================================================
        labelframe0_tab4 = ttk.LabelFrame(tab4, text = "Types of Test")
        labelframe0_tab4.grid(column = 0, row = 0, padx = 8, pady = 8, columnspan = 3)

        
        self.radVar1 = tk.IntVar()

        rad1 = tk.Radiobutton(labelframe0_tab4, text = "two_way" , variable=self.radVar1, value=1, command=self.radCall1)
        rad1.grid(column=0, row=0, sticky=tk.W)   

        rad2 = tk.Radiobutton(labelframe0_tab4, text = "left (P_1 < P_2)", variable=self.radVar1, value=2, command=self.radCall1)
        rad2.grid(column=1, row=0, sticky=tk.W)  

        rad3 = tk.Radiobutton(labelframe0_tab4,  text = "right (P_1 > P_2)", variable=self.radVar1, value=3, command=self.radCall1)
        rad3.grid(column=2, row=0, sticky=tk.W)
        
        
        
        # Frame1: Single Mean =====================================================================================
        # =========================================================================================================
        
        labelframe1_tab4 = ttk.LabelFrame(tab4, text = "Test for Single Proportion")
        labelframe1_tab4.grid(column = 0, row = 1, padx = 8, pady = 8)
        
        tab4_labels_left = ["p: ","p_hat : ","Sample Size : ", "Alpha : "]
        for r in range(len(tab4_labels_left)):
            ttk.Label(labelframe1_tab4, text = tab4_labels_left[r]).grid(column = 0, row = r, sticky = "W")
            

        self.tab4_single_p = tk.DoubleVar()
        self.tab4_single_p_entered = ttk.Entry(labelframe1_tab4, width = 12, textvariable = self.tab4_single_p)
        self.tab4_single_p_entered.grid(column = 1, row = 0, sticky = "W")

        self.tab4_single_p_hat = tk.DoubleVar()
        self.tab4_single_p_hat_entered = ttk.Entry(labelframe1_tab4, width = 12, textvariable = self.tab4_single_p_hat)
        self.tab4_single_p_hat_entered.grid(column = 1, row = 1, sticky = "W")
        
        self.tab4_single_n = tk.DoubleVar()
        self.tab4_single_n_entered = ttk.Entry(labelframe1_tab4, width = 12, textvariable = self.tab4_single_n)
        self.tab4_single_n_entered.grid(column = 1, row = 2, sticky = "W")
        
        self.tab4_single_alpha = tk.DoubleVar()
        self.tab4_single_alpha_entered = ttk.Entry(labelframe1_tab4, width = 12, textvariable = self.tab4_single_alpha)
        self.tab4_single_alpha_entered.grid(column = 1, row = 3, sticky = "W")
        
        self.excute7 = ttk.Button(labelframe1_tab4, text = "Run", command = self.one_z_test)
        self.excute7.grid(column = 1, row = 4, sticky = "E", columnspan = 2)

        
        
        
        
        
        # Frame2: Two Means =======================================================================================
        # =========================================================================================================

        labelframe2_tab4 = ttk.LabelFrame(tab4, text = "Test for Difference in Proportions")
        labelframe2_tab4.grid(column = 1, row = 1, padx = 8, pady = 8, columnspan = 2, rowspan = 2)
        
        # Names
        labelframe2_tab4_names = ttk.LabelFrame(labelframe2_tab4)
        labelframe2_tab4_names.grid(column =0, row = 0, padx = 4, pady = 4)
        # for sample 1
        labelframe2_tab4_sample1 = ttk.LabelFrame(labelframe2_tab4, text = "Sample 1")
        labelframe2_tab4_sample1.grid(column = 1, row = 0, padx = 4, pady = 4)
        # for sample 2
        labelframe2_tab4_sample2 = ttk.LabelFrame(labelframe2_tab4, text = "Sample 2")
        labelframe2_tab4_sample2.grid(column = 2, row = 0, padx = 4, pady = 4)
        # for alpha
        labelframe2_tab4_alpha = ttk.LabelFrame(labelframe2_tab4, text = "Alpha")
        labelframe2_tab4_alpha.grid(column = 0, row = 1, padx = 4, pady = 1, columnspan = 2)

        #labels
        tab4_names = ["p_hat : ", "Sample Size : "]
        
        for r in range(len(tab4_names)):
            ttk.Label(labelframe2_tab4_names, text = tab4_names[r]).grid(column = 0, row = r, sticky = "W")

        
        # for sample 1
        self.tab4_sample1_p_hat = tk.DoubleVar()
        self.tab4_sample1_p_hat_entered = ttk.Entry(labelframe2_tab4_sample1, width = 12, 
                                                   textvariable = self.tab4_sample1_p_hat)
        self.tab4_sample1_p_hat_entered.grid(column = 0, row = 0, sticky = "W")
        
        self.tab4_sample1_n = tk.DoubleVar()
        self.tab4_sample1_n_entered = ttk.Entry(labelframe2_tab4_sample1, width = 12, 
                                                 textvariable = self.tab4_sample1_n)
        self.tab4_sample1_n_entered.grid(column = 0, row = 1, sticky = "W")
        
        # for sample 2

        self.tab4_sample2_p_hat = tk.DoubleVar()
        self.tab4_sample2_p_hat_entered = ttk.Entry(labelframe2_tab4_sample2, width = 12, 
                                                   textvariable = self.tab4_sample2_p_hat)
        self.tab4_sample2_p_hat_entered.grid(column = 0, row = 0, sticky = "W")
        
        self.tab4_sample2_n = tk.DoubleVar()
        self.tab4_sample2_n_entered = ttk.Entry(labelframe2_tab4_sample2, width = 12, 
                                                 textvariable = self.tab4_sample2_n)
        self.tab4_sample2_n_entered.grid(column = 0, row = 1, sticky = "W")
        
        # for alpha
        ttk.Label(labelframe2_tab4_alpha, text = "Alpha :                  ").grid(column = 0, row = 0, sticky = "W")

        self.tab4_sample1_alpha = tk.DoubleVar()
        self.tab4_sample1_alpha_entered = ttk.Entry(labelframe2_tab4_alpha, width = 12, 
                                                    textvariable =self.tab4_sample1_alpha)
        self.tab4_sample1_alpha_entered.grid(column = 1, row = 0, sticky = "W")

        # run button
        self.excute8 = ttk.Button(labelframe2_tab4, text = "Run", command = self.two_z_test)
        self.excute8.grid(column = 2, row = 4 , sticky = "E")
        
        
        # =======================================
        # Answer ================================
        # =======================================
        
        tab4_answer = ttk.LabelFrame(tab4, text = "Answer")
        tab4_answer.grid(column = 0, row = 3, padx = 4, pady = 1, columnspan = 3)
        answer_tab4_names = ["z-test statistics : ", "rejection regions : ", "p-value : "]
        for r in range(len(answer_tab4_names)):
            ttk.Label(tab4_answer, text = answer_tab4_names[r]).grid(column = 0, row = r, sticky = "W")

        self.tab4_answer1 = ttk.Label(tab4_answer, text = "")
        self.tab4_answer1.grid(column = 1, row = 0)
        self.tab4_answer2 = ttk.Label(tab4_answer, text = "")
        self.tab4_answer2.grid(column = 1, row = 1)
        self.tab4_answer3= ttk.Label(tab4_answer, text = "")
        self.tab4_answer3.grid(column = 1, row = 2)
        
        
        
        
        
        

# =========================================
# Start GUI
# =========================================
if __name__ == "__main__":
    oop = OOP()
    oop.win.mainloop()
