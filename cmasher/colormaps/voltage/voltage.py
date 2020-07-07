# %% IMPORTS
# Package imports
from matplotlib.cm import register_cmap
from matplotlib.colors import ListedColormap

# All declaration
__all__ = ['cmap']

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"


# %% GLOBALS AND DEFINITIONS
# Type of this colormap (according to viscm)
cm_type = "linear"

# RGB-values of this colormap
cm_data = [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
           [3.12460050e-04, 2.01110207e-04, 2.56266737e-04],
           [1.12230605e-03, 6.81560586e-04, 9.05152133e-04],
           [2.39895820e-03, 1.38190201e-03, 1.90776936e-03],
           [4.13895357e-03, 2.27217151e-03, 3.25294407e-03],
           [6.34536547e-03, 3.33163092e-03, 4.93739711e-03],
           [9.02409170e-03, 4.54420798e-03, 6.96178741e-03],
           [1.21826707e-02, 5.89657661e-03, 9.32927110e-03],
           [1.58294489e-02, 7.37731187e-03, 1.20446826e-02],
           [1.99732529e-02, 8.97634990e-03, 1.51141322e-02],
           [2.46233965e-02, 1.06845617e-02, 1.85448635e-02],
           [2.97897928e-02, 1.24934238e-02, 2.23452305e-02],
           [3.54823687e-02, 1.43950806e-02, 2.65243629e-02],
           [4.16786389e-02, 1.63822647e-02, 3.10920519e-02],
           [4.79358206e-02, 1.84478269e-02, 3.60591705e-02],
           [5.41565416e-02, 2.05848959e-02, 4.14139699e-02],
           [6.03455729e-02, 2.27872430e-02, 4.68240939e-02],
           [6.65080804e-02, 2.50481740e-02, 5.22246857e-02],
           [7.26475298e-02, 2.73617570e-02, 5.76209361e-02],
           [7.87673662e-02, 2.97218982e-02, 6.30178589e-02],
           [8.48707535e-02, 3.21224703e-02, 6.84201681e-02],
           [9.09598860e-02, 3.45578863e-02, 7.38317747e-02],
           [9.70374820e-02, 3.70219620e-02, 7.92569424e-02],
           [1.03105157e-01, 3.95092539e-02, 8.46990445e-02],
           [1.09164898e-01, 4.19705611e-02, 9.01617324e-02],
           [1.15218366e-01, 4.43492692e-02, 9.56484053e-02],
           [1.21266497e-01, 4.66564513e-02, 1.01161843e-01],
           [1.27311422e-01, 4.88922167e-02, 1.06705909e-01],
           [1.33353532e-01, 5.10580701e-02, 1.12282955e-01],
           [1.39393829e-01, 5.31546197e-02, 1.17895903e-01],
           [1.45433737e-01, 5.51817276e-02, 1.23548147e-01],
           [1.51473722e-01, 5.71399998e-02, 1.29242228e-01],
           [1.57514348e-01, 5.90297065e-02, 1.34980826e-01],
           [1.63556256e-01, 6.08507983e-02, 1.40766768e-01],
           [1.69599998e-01, 6.26030983e-02, 1.46602871e-01],
           [1.75646112e-01, 6.42862219e-02, 1.52492026e-01],
           [1.81695001e-01, 6.58997202e-02, 1.58437081e-01],
           [1.87746773e-01, 6.74432999e-02, 1.64440639e-01],
           [1.93801638e-01, 6.89163478e-02, 1.70505517e-01],
           [1.99859720e-01, 7.03181530e-02, 1.76634541e-01],
           [2.05921060e-01, 7.16479107e-02, 1.82830549e-01],
           [2.11985867e-01, 7.29043736e-02, 1.89096730e-01],
           [2.18053879e-01, 7.40867233e-02, 1.95435806e-01],
           [2.24124842e-01, 7.51939317e-02, 2.01850633e-01],
           [2.30198442e-01, 7.62248553e-02, 2.08344120e-01],
           [2.36274267e-01, 7.71782818e-02, 2.14919186e-01],
           [2.42352534e-01, 7.80517714e-02, 2.21579863e-01],
           [2.48432025e-01, 7.88448776e-02, 2.28328241e-01],
           [2.54512222e-01, 7.95558459e-02, 2.35167603e-01],
           [2.60592841e-01, 8.01822320e-02, 2.42101835e-01],
           [2.66672415e-01, 8.07233430e-02, 2.49133116e-01],
           [2.72750645e-01, 8.11761744e-02, 2.56265771e-01],
           [2.78825999e-01, 8.15396243e-02, 2.63502274e-01],
           [2.84897228e-01, 8.18118326e-02, 2.70845773e-01],
           [2.90963584e-01, 8.19895860e-02, 2.78300650e-01],
           [2.97023020e-01, 8.20719247e-02, 2.85869120e-01],
           [3.03073952e-01, 8.20566661e-02, 2.93554514e-01],
           [3.09114595e-01, 8.19416932e-02, 3.01360070e-01],
           [3.15142954e-01, 8.17249993e-02, 3.09288899e-01],
           [3.21156803e-01, 8.14047407e-02, 3.17343945e-01],
           [3.27153682e-01, 8.09793010e-02, 3.25527948e-01],
           [3.33130878e-01, 8.04473661e-02, 3.33843394e-01],
           [3.39085417e-01, 7.98080139e-02, 3.42292465e-01],
           [3.45014255e-01, 7.90602196e-02, 3.50877525e-01],
           [3.50914020e-01, 7.82036131e-02, 3.59600480e-01],
           [3.56780594e-01, 7.72400002e-02, 3.68461493e-01],
           [3.62610507e-01, 7.61690557e-02, 3.77462904e-01],
           [3.68398877e-01, 7.49952225e-02, 3.86603221e-01],
           [3.74141515e-01, 7.37208389e-02, 3.95883312e-01],
           [3.79833268e-01, 7.23522377e-02, 4.05301231e-01],
           [3.85468888e-01, 7.08970343e-02, 4.14854793e-01],
           [3.91042906e-01, 6.93649234e-02, 4.24541120e-01],
           [3.96549562e-01, 6.77684823e-02, 4.34356231e-01],
           [4.01982837e-01, 6.61236406e-02, 4.44294979e-01],
           [4.07336505e-01, 6.44501720e-02, 4.54350993e-01],
           [4.12604182e-01, 6.27721808e-02, 4.64516650e-01],
           [4.17779395e-01, 6.11185481e-02, 4.74783068e-01],
           [4.22855648e-01, 5.95232761e-02, 4.85140133e-01],
           [4.27826590e-01, 5.80248632e-02, 4.95577174e-01],
           [4.32685822e-01, 5.66684761e-02, 5.06081251e-01],
           [4.37427257e-01, 5.55032536e-02, 5.16638997e-01],
           [4.42045129e-01, 5.45816498e-02, 5.27236480e-01],
           [4.46533967e-01, 5.39592239e-02, 5.37858240e-01],
           [4.50888826e-01, 5.36902692e-02, 5.48489177e-01],
           [4.55105222e-01, 5.38270115e-02, 5.59113166e-01],
           [4.59179265e-01, 5.44150657e-02, 5.69714505e-01],
           [4.63107656e-01, 5.54913704e-02, 5.80277419e-01],
           [4.66887720e-01, 5.70814523e-02, 5.90786584e-01],
           [4.70517411e-01, 5.91981185e-02, 6.01227244e-01],
           [4.73995299e-01, 6.18411697e-02, 6.11585452e-01],
           [4.77320556e-01, 6.49985143e-02, 6.21848022e-01],
           [4.80492905e-01, 6.86477547e-02, 6.32002975e-01],
           [4.83512597e-01, 7.27588918e-02, 6.42039267e-01],
           [4.86380353e-01, 7.72967150e-02, 6.51947052e-01],
           [4.89097304e-01, 8.22232264e-02, 6.61717665e-01],
           [4.91664958e-01, 8.74996826e-02, 6.71343526e-01],
           [4.94085138e-01, 9.30880875e-02, 6.80818164e-01],
           [4.96359871e-01, 9.89522193e-02, 6.90136384e-01],
           [4.98491556e-01, 1.05058466e-01, 6.99293426e-01],
           [5.00482542e-01, 1.11375904e-01, 7.08286233e-01],
           [5.02335426e-01, 1.17876660e-01, 7.17112163e-01],
           [5.04053026e-01, 1.24535724e-01, 7.25769072e-01],
           [5.05637974e-01, 1.31330853e-01, 7.34256165e-01],
           [5.07093069e-01, 1.38242369e-01, 7.42572922e-01],
           [5.08421126e-01, 1.45252910e-01, 7.50719379e-01],
           [5.09624958e-01, 1.52347200e-01, 7.58696060e-01],
           [5.10707361e-01, 1.59511825e-01, 7.66503910e-01],
           [5.11671096e-01, 1.66735022e-01, 7.74144241e-01],
           [5.12518881e-01, 1.74006481e-01, 7.81618670e-01],
           [5.13253384e-01, 1.81317177e-01, 7.88929074e-01],
           [5.13877212e-01, 1.88659208e-01, 7.96077541e-01],
           [5.14392911e-01, 1.96025659e-01, 8.03066329e-01],
           [5.14802960e-01, 2.03410482e-01, 8.09897830e-01],
           [5.15109774e-01, 2.10808385e-01, 8.16574536e-01],
           [5.15315698e-01, 2.18214742e-01, 8.23099012e-01],
           [5.15423013e-01, 2.25625508e-01, 8.29473866e-01],
           [5.15434148e-01, 2.33036992e-01, 8.35701593e-01],
           [5.15351070e-01, 2.40446248e-01, 8.41784976e-01],
           [5.15175858e-01, 2.47850591e-01, 8.47726648e-01],
           [5.14910682e-01, 2.55247585e-01, 8.53529141e-01],
           [5.14557544e-01, 2.62635175e-01, 8.59195020e-01],
           [5.14118222e-01, 2.70011702e-01, 8.64726872e-01],
           [5.13594815e-01, 2.77375482e-01, 8.70127062e-01],
           [5.12989043e-01, 2.84725280e-01, 8.75398031e-01],
           [5.12302690e-01, 2.92059969e-01, 8.80542092e-01],
           [5.11537681e-01, 2.99378469e-01, 8.85561429e-01],
           [5.10695518e-01, 3.06680109e-01, 8.90458245e-01],
           [5.09778215e-01, 3.13963989e-01, 8.95234522e-01],
           [5.08787144e-01, 3.21229728e-01, 8.99892275e-01],
           [5.07724300e-01, 3.28476633e-01, 9.04433304e-01],
           [5.06591056e-01, 3.35704490e-01, 9.08859397e-01],
           [5.05389362e-01, 3.42912796e-01, 9.13172168e-01],
           [5.04120653e-01, 3.50101439e-01, 9.17373171e-01],
           [5.02786813e-01, 3.57270097e-01, 9.21463817e-01],
           [5.01389419e-01, 3.64418695e-01, 9.25445423e-01],
           [4.99930300e-01, 3.71547070e-01, 9.29319186e-01],
           [4.98411211e-01, 3.78655157e-01, 9.33086190e-01],
           [4.96833982e-01, 3.85742910e-01, 9.36747400e-01],
           [4.95200557e-01, 3.92810272e-01, 9.40303671e-01],
           [4.93512855e-01, 3.99857260e-01, 9.43755732e-01],
           [4.91772995e-01, 4.06883837e-01, 9.47104204e-01],
           [4.89983103e-01, 4.13890029e-01, 9.50349582e-01],
           [4.88145473e-01, 4.20875829e-01, 9.53492247e-01],
           [4.86262513e-01, 4.27841241e-01, 9.56532459e-01],
           [4.84336801e-01, 4.34786248e-01, 9.59470365e-01],
           [4.82371019e-01, 4.41710855e-01, 9.62305981e-01],
           [4.80368157e-01, 4.48614989e-01, 9.65039233e-01],
           [4.78331244e-01, 4.55498642e-01, 9.67669888e-01],
           [4.76263725e-01, 4.62361689e-01, 9.70197646e-01],
           [4.74169153e-01, 4.69204052e-01, 9.72622055e-01],
           [4.72051436e-01, 4.76025581e-01, 9.74942568e-01],
           [4.69914807e-01, 4.82826084e-01, 9.77158539e-01],
           [4.67763718e-01, 4.89605383e-01, 9.79269170e-01],
           [4.65603214e-01, 4.96363151e-01, 9.81273641e-01],
           [4.63438419e-01, 5.03099158e-01, 9.83170914e-01],
           [4.61275294e-01, 5.09812938e-01, 9.84960010e-01],
           [4.59119813e-01, 5.16504171e-01, 9.86639678e-01],
           [4.56978932e-01, 5.23172262e-01, 9.88208789e-01],
           [4.54859699e-01, 5.29816745e-01, 9.89665940e-01],
           [4.52770110e-01, 5.36436919e-01, 9.91009837e-01],
           [4.50718550e-01, 5.43032103e-01, 9.92239028e-01],
           [4.48714064e-01, 5.49601527e-01, 9.93352024e-01],
           [4.46766648e-01, 5.56144220e-01, 9.94347469e-01],
           [4.44886387e-01, 5.62659376e-01, 9.95223648e-01],
           [4.43084868e-01, 5.69145772e-01, 9.95979309e-01],
           [4.41373968e-01, 5.75602276e-01, 9.96612980e-01],
           [4.39766195e-01, 5.82027700e-01, 9.97123161e-01],
           [4.38275274e-01, 5.88420557e-01, 9.97508765e-01],
           [4.36915382e-01, 5.94779369e-01, 9.97768656e-01],
           [4.35701179e-01, 6.01102639e-01, 9.97901683e-01],
           [4.34648433e-01, 6.07388571e-01, 9.97907266e-01],
           [4.33773280e-01, 6.13635348e-01, 9.97784927e-01],
           [4.33092318e-01, 6.19841062e-01, 9.97534477e-01],
           [4.32622431e-01, 6.26003736e-01, 9.97156005e-01],
           [4.32380860e-01, 6.32121250e-01, 9.96650157e-01],
           [4.32384872e-01, 6.38191407e-01, 9.96018056e-01],
           [4.32651509e-01, 6.44211975e-01, 9.95261305e-01],
           [4.33197411e-01, 6.50180681e-01, 9.94382098e-01],
           [4.34038559e-01, 6.56095231e-01, 9.93383274e-01],
           [4.35190001e-01, 6.61953343e-01, 9.92268365e-01],
           [4.36665561e-01, 6.67752774e-01, 9.91041629e-01],
           [4.38477580e-01, 6.73491343e-01, 9.89708140e-01],
           [4.40636584e-01, 6.79166989e-01, 9.88273711e-01],
           [4.43151054e-01, 6.84777803e-01, 9.86744935e-01],
           [4.46027196e-01, 6.90322060e-01, 9.85129164e-01],
           [4.49268759e-01, 6.95798266e-01, 9.83434470e-01],
           [4.52876909e-01, 7.01205188e-01, 9.81669584e-01],
           [4.56850173e-01, 7.06541867e-01, 9.79843979e-01],
           [4.61184407e-01, 7.11807685e-01, 9.77967522e-01],
           [4.65872904e-01, 7.17002397e-01, 9.76050287e-01],
           [4.70906553e-01, 7.22126098e-01, 9.74102665e-01],
           [4.76273964e-01, 7.27179205e-01, 9.72135570e-01],
           [4.81961777e-01, 7.32162534e-01, 9.70159664e-01],
           [4.87955128e-01, 7.37077305e-01, 9.68184792e-01],
           [4.94237374e-01, 7.41924927e-01, 9.66222262e-01],
           [5.00791460e-01, 7.46707288e-01, 9.64280745e-01],
           [5.07598898e-01, 7.51426397e-01, 9.62370830e-01],
           [5.14641707e-01, 7.56084633e-01, 9.60500039e-01],
           [5.21900770e-01, 7.60684470e-01, 9.58677983e-01],
           [5.29357967e-01, 7.65228625e-01, 9.56911554e-01],
           [5.36995408e-01, 7.69719915e-01, 9.55207464e-01],
           [5.44795595e-01, 7.74161244e-01, 9.53572121e-01],
           [5.52741752e-01, 7.78555582e-01, 9.52011224e-01],
           [5.60817960e-01, 7.82905933e-01, 9.50529757e-01],
           [5.69009254e-01, 7.87215299e-01, 9.49131993e-01],
           [5.77301690e-01, 7.91486659e-01, 9.47821516e-01],
           [5.85682383e-01, 7.95722939e-01, 9.46601248e-01],
           [5.94139526e-01, 7.99926995e-01, 9.45473488e-01],
           [6.02661938e-01, 8.04101638e-01, 9.44440569e-01],
           [6.11238727e-01, 8.08249672e-01, 9.43505263e-01],
           [6.19862328e-01, 8.12373555e-01, 9.42666602e-01],
           [6.28522601e-01, 8.16476024e-01, 9.41927970e-01],
           [6.37214033e-01, 8.20559270e-01, 9.41287329e-01],
           [6.45927485e-01, 8.24625931e-01, 9.40748097e-01],
           [6.54658978e-01, 8.28677964e-01, 9.40307704e-01],
           [6.63402753e-01, 8.32717536e-01, 9.39966517e-01],
           [6.72152385e-01, 8.36746925e-01, 9.39726200e-01],
           [6.80905064e-01, 8.40767848e-01, 9.39584519e-01],
           [6.89656841e-01, 8.44782172e-01, 9.39541121e-01],
           [6.98404261e-01, 8.48791671e-01, 9.39595484e-01],
           [7.07144319e-01, 8.52798027e-01, 9.39746940e-01],
           [7.15874422e-01, 8.56802837e-01, 9.39994695e-01],
           [7.24592356e-01, 8.60807608e-01, 9.40337846e-01],
           [7.33296245e-01, 8.64813769e-01, 9.40775402e-01],
           [7.41984517e-01, 8.68822668e-01, 9.41306300e-01],
           [7.50655880e-01, 8.72835581e-01, 9.41929421e-01],
           [7.59307445e-01, 8.76854092e-01, 9.42645562e-01],
           [7.67939896e-01, 8.80879043e-01, 9.43451876e-01],
           [7.76552609e-01, 8.84911508e-01, 9.44347135e-01],
           [7.85143494e-01, 8.88952866e-01, 9.45331796e-01],
           [7.93712457e-01, 8.93004050e-01, 9.46404369e-01],
           [8.02260105e-01, 8.97065810e-01, 9.47562794e-01],
           [8.10783464e-01, 9.01139690e-01, 9.48808806e-01],
           [8.19285449e-01, 9.05225872e-01, 9.50138242e-01],
           [8.27762275e-01, 9.09326076e-01, 9.51553841e-01],
           [8.36217015e-01, 9.13440389e-01, 9.53051524e-01],
           [8.44647053e-01, 9.17570240e-01, 9.54633003e-01],
           [8.53053580e-01, 9.21716129e-01, 9.56296276e-01],
           [8.61437023e-01, 9.25878712e-01, 9.58040196e-01],
           [8.69794782e-01, 9.30059404e-01, 9.59866622e-01],
           [8.78129113e-01, 9.34258378e-01, 9.61772754e-01],
           [8.86439724e-01, 9.38476435e-01, 9.63758343e-01],
           [8.94725548e-01, 9.42714570e-01, 9.65823928e-01],
           [9.02986301e-01, 9.46973572e-01, 9.67969340e-01],
           [9.11222625e-01, 9.51253965e-01, 9.70193596e-01],
           [9.19434146e-01, 9.55556535e-01, 9.72496730e-01],
           [9.27620420e-01, 9.59882079e-01, 9.74878886e-01],
           [9.35780912e-01, 9.64231414e-01, 9.77340340e-01],
           [9.43914962e-01, 9.68605382e-01, 9.79881533e-01],
           [9.52021391e-01, 9.73004973e-01, 9.82503424e-01],
           [9.60099542e-01, 9.77431022e-01, 9.85206546e-01],
           [9.68148158e-01, 9.81884533e-01, 9.87992024e-01],
           [9.76165441e-01, 9.86366669e-01, 9.90861509e-01],
           [9.84148975e-01, 9.90878781e-01, 9.93817207e-01],
           [9.92095425e-01, 9.95422514e-01, 9.96862062e-01],
           [1.00000000e+00, 1.00000000e+00, 1.00000000e+00]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.voltage", N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
