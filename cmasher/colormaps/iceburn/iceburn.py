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
cm_type = "diverging"

# RGB-values of this colormap
cm_data = [[5.78692840e-01, 9.47004534e-01, 9.53835089e-01],
           [5.73300958e-01, 9.42448134e-01, 9.52185844e-01],
           [5.67904138e-01, 9.37906186e-01, 9.50550251e-01],
           [5.62501828e-01, 9.33378441e-01, 9.48929504e-01],
           [5.57094001e-01, 9.28864700e-01, 9.47323254e-01],
           [5.51680262e-01, 9.24364725e-01, 9.45732234e-01],
           [5.46260408e-01, 9.19878293e-01, 9.44156633e-01],
           [5.40834283e-01, 9.15405185e-01, 9.42596495e-01],
           [5.35401418e-01, 9.10945148e-01, 9.41052774e-01],
           [5.29961833e-01, 9.06497972e-01, 9.39525036e-01],
           [5.24515168e-01, 9.02063412e-01, 9.38013919e-01],
           [5.19061153e-01, 8.97641224e-01, 9.36519804e-01],
           [5.13599714e-01, 8.93231185e-01, 9.35042546e-01],
           [5.08130514e-01, 8.88833041e-01, 9.33582712e-01],
           [5.02653292e-01, 8.84446544e-01, 9.32140656e-01],
           [4.97167970e-01, 8.80071461e-01, 9.30716251e-01],
           [4.91674325e-01, 8.75707544e-01, 9.29309753e-01],
           [4.86171948e-01, 8.71354522e-01, 9.27921902e-01],
           [4.80660799e-01, 8.67012158e-01, 9.26552467e-01],
           [4.75140686e-01, 8.62680199e-01, 9.25201622e-01],
           [4.69611394e-01, 8.58358385e-01, 9.23869585e-01],
           [4.64072657e-01, 8.54046451e-01, 9.22556718e-01],
           [4.58524236e-01, 8.49744130e-01, 9.21263293e-01],
           [4.52966030e-01, 8.45451166e-01, 9.19989242e-01],
           [4.47397837e-01, 8.41167290e-01, 9.18734745e-01],
           [4.41819459e-01, 8.36892232e-01, 9.17499973e-01],
           [4.36230702e-01, 8.32625718e-01, 9.16285085e-01],
           [4.30631373e-01, 8.28367471e-01, 9.15090231e-01],
           [4.25021288e-01, 8.24117213e-01, 9.13915551e-01],
           [4.19400262e-01, 8.19874661e-01, 9.12761172e-01],
           [4.13768119e-01, 8.15639529e-01, 9.11627211e-01],
           [4.08124687e-01, 8.11411529e-01, 9.10513772e-01],
           [4.02469802e-01, 8.07190370e-01, 9.09420950e-01],
           [3.96803304e-01, 8.02975757e-01, 9.08348825e-01],
           [3.91125045e-01, 7.98767391e-01, 9.07297464e-01],
           [3.85434884e-01, 7.94564972e-01, 9.06266924e-01],
           [3.79732689e-01, 7.90368192e-01, 9.05257244e-01],
           [3.74018344e-01, 7.86176744e-01, 9.04268451e-01],
           [3.68291742e-01, 7.81990315e-01, 9.03300558e-01],
           [3.62552792e-01, 7.77808588e-01, 9.02353560e-01],
           [3.56801422e-01, 7.73631242e-01, 9.01427436e-01],
           [3.51037448e-01, 7.69457933e-01, 9.00522481e-01],
           [3.45260887e-01, 7.65288338e-01, 8.99638516e-01],
           [3.39471788e-01, 7.61122132e-01, 8.98775317e-01],
           [3.33670169e-01, 7.56958978e-01, 8.97932792e-01],
           [3.27855879e-01, 7.52798495e-01, 8.97111369e-01],
           [3.22029122e-01, 7.48640355e-01, 8.96310603e-01],
           [3.16190082e-01, 7.44484220e-01, 8.95530166e-01],
           [3.10338662e-01, 7.40329674e-01, 8.94770632e-01],
           [3.04475280e-01, 7.36176394e-01, 8.94031249e-01],
           [2.98600109e-01, 7.32023987e-01, 8.93312085e-01],
           [2.92713429e-01, 7.27872062e-01, 8.92613085e-01],
           [2.86815720e-01, 7.23720253e-01, 8.91933779e-01],
           [2.80907351e-01, 7.19568136e-01, 8.91274268e-01],
           [2.74988962e-01, 7.15415329e-01, 8.90634084e-01],
           [2.69061237e-01, 7.11261425e-01, 8.90012916e-01],
           [2.63124858e-01, 7.07105970e-01, 8.89410864e-01],
           [2.57180924e-01, 7.02948593e-01, 8.88827028e-01],
           [2.51230430e-01, 6.98788826e-01, 8.88261402e-01],
           [2.45274625e-01, 6.94626213e-01, 8.87713728e-01],
           [2.39315083e-01, 6.90460341e-01, 8.87183219e-01],
           [2.33353507e-01, 6.86290746e-01, 8.86669459e-01],
           [2.27391881e-01, 6.82116958e-01, 8.86171983e-01],
           [2.21432481e-01, 6.77938476e-01, 8.85690423e-01],
           [2.15477996e-01, 6.73754829e-01, 8.85224061e-01],
           [2.09531518e-01, 6.69565533e-01, 8.84772141e-01],
           [2.03596591e-01, 6.65370084e-01, 8.84333945e-01],
           [1.97677299e-01, 6.61167973e-01, 8.83908683e-01],
           [1.91778351e-01, 6.56958680e-01, 8.83495480e-01],
           [1.85905169e-01, 6.52741636e-01, 8.83093687e-01],
           [1.80064006e-01, 6.48516336e-01, 8.82702059e-01],
           [1.74262029e-01, 6.44282242e-01, 8.82319418e-01],
           [1.68507468e-01, 6.40038815e-01, 8.81944496e-01],
           [1.62809859e-01, 6.35785434e-01, 8.81576365e-01],
           [1.57180072e-01, 6.31521552e-01, 8.81213460e-01],
           [1.51630475e-01, 6.27246648e-01, 8.80853939e-01],
           [1.46175578e-01, 6.22960017e-01, 8.80496851e-01],
           [1.40831375e-01, 6.18661207e-01, 8.80139636e-01],
           [1.35616639e-01, 6.14349529e-01, 8.79780903e-01],
           [1.30552271e-01, 6.10024426e-01, 8.79418327e-01],
           [1.25661794e-01, 6.05685341e-01, 8.79049446e-01],
           [1.20971707e-01, 6.01331668e-01, 8.78671861e-01],
           [1.16511563e-01, 5.96962778e-01, 8.78283072e-01],
           [1.12313402e-01, 5.92578135e-01, 8.77879944e-01],
           [1.08411955e-01, 5.88177194e-01, 8.77459198e-01],
           [1.04844299e-01, 5.83759401e-01, 8.77017401e-01],
           [1.01649143e-01, 5.79324204e-01, 8.76550875e-01],
           [9.88650977e-02, 5.74871174e-01, 8.76055248e-01],
           [9.65299433e-02, 5.70399900e-01, 8.75525883e-01],
           [9.46800608e-02, 5.65909873e-01, 8.74958273e-01],
           [9.33458797e-02, 5.61400868e-01, 8.74346664e-01],
           [9.25534686e-02, 5.56872508e-01, 8.73685607e-01],
           [9.23193790e-02, 5.52324723e-01, 8.72968423e-01],
           [9.26524359e-02, 5.47757391e-01, 8.72188384e-01],
           [9.35518714e-02, 5.43170516e-01, 8.71338162e-01],
           [9.50066950e-02, 5.38564305e-01, 8.70409626e-01],
           [9.69974085e-02, 5.33939078e-01, 8.69394153e-01],
           [9.94960176e-02, 5.29295411e-01, 8.68282281e-01],
           [1.02468098e-01, 5.24634109e-01, 8.67063874e-01],
           [1.05875414e-01, 5.19956133e-01, 8.65728330e-01],
           [1.09675761e-01, 5.15262814e-01, 8.64264188e-01],
           [1.13825799e-01, 5.10555737e-01, 8.62659495e-01],
           [1.18280497e-01, 5.05836943e-01, 8.60901548e-01],
           [1.22995807e-01, 5.01108771e-01, 8.58977360e-01],
           [1.27928180e-01, 4.96373991e-01, 8.56873612e-01],
           [1.33034952e-01, 4.91635812e-01, 8.54576873e-01],
           [1.38274606e-01, 4.86897881e-01, 8.52073885e-01],
           [1.43607170e-01, 4.82164234e-01, 8.49351901e-01],
           [1.48994245e-01, 4.77439269e-01, 8.46399020e-01],
           [1.54397994e-01, 4.72727808e-01, 8.43204529e-01],
           [1.59783445e-01, 4.68034774e-01, 8.39759425e-01],
           [1.65116349e-01, 4.63365350e-01, 8.36056706e-01],
           [1.70365215e-01, 4.58724648e-01, 8.32091774e-01],
           [1.75500824e-01, 4.54117670e-01, 8.27862671e-01],
           [1.80496667e-01, 4.49549147e-01, 8.23370253e-01],
           [1.85329435e-01, 4.45023391e-01, 8.18618195e-01],
           [1.89978991e-01, 4.40544209e-01, 8.13612915e-01],
           [1.94429078e-01, 4.36114753e-01, 8.08363251e-01],
           [1.98666394e-01, 4.31737576e-01, 8.02880303e-01],
           [2.02681886e-01, 4.27414456e-01, 7.97176723e-01],
           [2.06468728e-01, 4.23146613e-01, 7.91266744e-01],
           [2.10024161e-01, 4.18934517e-01, 7.85165130e-01],
           [2.13347437e-01, 4.14778131e-01, 7.78887270e-01],
           [2.16440070e-01, 4.10676919e-01, 7.72448643e-01],
           [2.19305491e-01, 4.06629916e-01, 7.65864489e-01],
           [2.21948709e-01, 4.02635810e-01, 7.59149540e-01],
           [2.24375980e-01, 3.98693013e-01, 7.52317815e-01],
           [2.26593924e-01, 3.94799781e-01, 7.45382836e-01],
           [2.28610197e-01, 3.90954195e-01, 7.38357023e-01],
           [2.30432432e-01, 3.87154276e-01, 7.31252161e-01],
           [2.32068926e-01, 3.83397966e-01, 7.24078812e-01],
           [2.33527523e-01, 3.79683233e-01, 7.16847009e-01],
           [2.34816084e-01, 3.76008051e-01, 7.09565901e-01],
           [2.35942398e-01, 3.72370426e-01, 7.02243776e-01],
           [2.36914105e-01, 3.68768412e-01, 6.94888104e-01],
           [2.37738643e-01, 3.65200126e-01, 6.87505580e-01],
           [2.38422282e-01, 3.61663789e-01, 6.80103136e-01],
           [2.38972594e-01, 3.58157636e-01, 6.72685501e-01],
           [2.39395009e-01, 3.54680041e-01, 6.65258749e-01],
           [2.39696225e-01, 3.51229407e-01, 6.57826776e-01],
           [2.39881773e-01, 3.47804242e-01, 6.50393943e-01],
           [2.39956943e-01, 3.44403123e-01, 6.42964150e-01],
           [2.39926779e-01, 3.41024699e-01, 6.35540879e-01],
           [2.39796090e-01, 3.37667689e-01, 6.28127227e-01],
           [2.39569444e-01, 3.34330882e-01, 6.20725937e-01],
           [2.39251183e-01, 3.31013128e-01, 6.13339431e-01],
           [2.38845424e-01, 3.27713344e-01, 6.05969844e-01],
           [2.38355808e-01, 3.24430499e-01, 5.98619437e-01],
           [2.37785799e-01, 3.21163615e-01, 5.91290231e-01],
           [2.37139189e-01, 3.17911780e-01, 5.83983238e-01],
           [2.36418594e-01, 3.14674104e-01, 5.76700831e-01],
           [2.35627508e-01, 3.11449771e-01, 5.69443559e-01],
           [2.34768626e-01, 3.08237993e-01, 5.62212823e-01],
           [2.33844361e-01, 3.05038009e-01, 5.55010144e-01],
           [2.32857559e-01, 3.01849126e-01, 5.47835919e-01],
           [2.31810546e-01, 2.98670665e-01, 5.40691084e-01],
           [2.30705538e-01, 2.95501982e-01, 5.33576454e-01],
           [2.29544644e-01, 2.92342466e-01, 5.26492728e-01],
           [2.28329868e-01, 2.89191531e-01, 5.19440505e-01],
           [2.27063120e-01, 2.86048621e-01, 5.12420289e-01],
           [2.25746215e-01, 2.82913203e-01, 5.05432497e-01],
           [2.24380878e-01, 2.79784770e-01, 4.98477470e-01],
           [2.22968752e-01, 2.76662836e-01, 4.91555475e-01],
           [2.21511396e-01, 2.73546937e-01, 4.84666715e-01],
           [2.20010239e-01, 2.70436621e-01, 4.77811461e-01],
           [2.18466444e-01, 2.67331436e-01, 4.70990359e-01],
           [2.16881625e-01, 2.64230995e-01, 4.64202867e-01],
           [2.15256985e-01, 2.61134895e-01, 4.57449146e-01],
           [2.13593418e-01, 2.58042718e-01, 4.50729909e-01],
           [2.11892450e-01, 2.54954135e-01, 4.44044228e-01],
           [2.10154732e-01, 2.51868737e-01, 4.37393064e-01],
           [2.08381656e-01, 2.48786217e-01, 4.30775450e-01],
           [2.06573793e-01, 2.45706187e-01, 4.24192274e-01],
           [2.04732430e-01, 2.42628362e-01, 4.17642496e-01],
           [2.02858067e-01, 2.39552372e-01, 4.11126922e-01],
           [2.00951756e-01, 2.36477929e-01, 4.04644823e-01],
           [1.99014302e-01, 2.33404731e-01, 3.98195962e-01],
           [1.97046147e-01, 2.30332431e-01, 3.91780945e-01],
           [1.95048234e-01, 2.27260766e-01, 3.85398932e-01],
           [1.93021210e-01, 2.24189441e-01, 3.79049751e-01],
           [1.90965676e-01, 2.21118165e-01, 3.72733244e-01],
           [1.88882068e-01, 2.18046628e-01, 3.66449615e-01],
           [1.86771070e-01, 2.14974566e-01, 3.60198266e-01],
           [1.84633214e-01, 2.11901701e-01, 3.53978926e-01],
           [1.82468982e-01, 2.08827751e-01, 3.47791363e-01],
           [1.80278832e-01, 2.05752438e-01, 3.41635323e-01],
           [1.78063194e-01, 2.02675486e-01, 3.35510539e-01],
           [1.75822472e-01, 1.99596616e-01, 3.29416728e-01],
           [1.73557047e-01, 1.96515552e-01, 3.23353592e-01],
           [1.71267273e-01, 1.93432015e-01, 3.17320821e-01],
           [1.68953481e-01, 1.90345728e-01, 3.11318090e-01],
           [1.66615979e-01, 1.87256408e-01, 3.05345062e-01],
           [1.64255048e-01, 1.84163774e-01, 2.99401390e-01],
           [1.61870950e-01, 1.81067539e-01, 2.93486714e-01],
           [1.59463922e-01, 1.77967413e-01, 2.87600662e-01],
           [1.57034176e-01, 1.74863103e-01, 2.81742854e-01],
           [1.54581876e-01, 1.71754305e-01, 2.75912999e-01],
           [1.52107134e-01, 1.68640705e-01, 2.70110883e-01],
           [1.49610173e-01, 1.65522006e-01, 2.64335837e-01],
           [1.47091119e-01, 1.62397894e-01, 2.58587437e-01],
           [1.44550070e-01, 1.59268044e-01, 2.52865249e-01],
           [1.41987011e-01, 1.56132104e-01, 2.47169165e-01],
           [1.39402031e-01, 1.52989740e-01, 2.41498612e-01],
           [1.36795217e-01, 1.49840614e-01, 2.35852930e-01],
           [1.34166545e-01, 1.46684356e-01, 2.30231753e-01],
           [1.31515885e-01, 1.43520568e-01, 2.24635009e-01],
           [1.28843336e-01, 1.40348896e-01, 2.19061687e-01],
           [1.26148778e-01, 1.37168927e-01, 2.13511466e-01],
           [1.23432032e-01, 1.33980228e-01, 2.07984146e-01],
           [1.20693111e-01, 1.30782396e-01, 2.02478680e-01],
           [1.17931726e-01, 1.27574952e-01, 1.96995048e-01],
           [1.15147777e-01, 1.24357446e-01, 1.91532377e-01],
           [1.12341037e-01, 1.21129384e-01, 1.86090147e-01],
           [1.09511209e-01, 1.17890242e-01, 1.80667973e-01],
           [1.06658103e-01, 1.14639504e-01, 1.75264889e-01],
           [1.03781280e-01, 1.11376578e-01, 1.69880751e-01],
           [1.00880520e-01, 1.08100903e-01, 1.64514367e-01],
           [9.79552928e-02, 1.04811822e-01, 1.59165616e-01],
           [9.50052857e-02, 1.01508706e-01, 1.53833276e-01],
           [9.20299100e-02, 9.81908332e-02, 1.48517042e-01],
           [8.90287064e-02, 9.48574837e-02, 1.43215838e-01],
           [8.60010553e-02, 9.15078661e-02, 1.37928993e-01],
           [8.29462963e-02, 8.81411436e-02, 1.32655723e-01],
           [7.98637948e-02, 8.47564453e-02, 1.27394821e-01],
           [7.67526386e-02, 8.13527897e-02, 1.22145928e-01],
           [7.36121083e-02, 7.79291923e-02, 1.16907471e-01],
           [7.04412107e-02, 7.44845475e-02, 1.11678639e-01],
           [6.72388963e-02, 7.10176749e-02, 1.06458404e-01],
           [6.40041036e-02, 6.75273224e-02, 1.01245258e-01],
           [6.07355301e-02, 6.40121018e-02, 9.60381728e-02],
           [5.74318124e-02, 6.04705226e-02, 9.08357274e-02],
           [5.40914827e-02, 5.69009698e-02, 8.56362070e-02],
           [5.07128356e-02, 5.33016572e-02, 8.04381104e-02],
           [4.72939791e-02, 4.96706236e-02, 7.52397997e-02],
           [4.38328995e-02, 4.60057289e-02, 7.00390473e-02],
           [4.03253250e-02, 4.23045858e-02, 6.48337039e-02],
           [3.68119799e-02, 3.85588031e-02, 5.96215760e-02],
           [3.34383800e-02, 3.49234868e-02, 5.43999018e-02],
           [3.02065532e-02, 3.14566306e-02, 4.91655596e-02],
           [2.71185916e-02, 2.81589142e-02, 4.39151506e-02],
           [2.41766866e-02, 2.50311454e-02, 3.86382927e-02],
           [2.13831525e-02, 2.20742794e-02, 3.36012698e-02],
           [1.87405026e-02, 1.92894533e-02, 2.89448430e-02],
           [1.62514037e-02, 1.66779945e-02, 2.46610222e-02],
           [1.39187470e-02, 1.42414639e-02, 2.07420804e-02],
           [1.17456978e-02, 1.19817007e-02, 1.71805773e-02],
           [9.73575395e-03, 9.90087988e-03, 1.39694399e-02],
           [7.89285303e-03, 8.00159702e-03, 1.11018863e-02],
           [6.22148215e-03, 6.28697637e-03, 8.57157164e-03],
           [4.72684477e-03, 4.76082980e-03, 6.37274354e-03],
           [3.41513042e-03, 3.42790180e-03, 4.50037440e-03],
           [2.29393772e-03, 2.29426270e-03, 2.95045739e-03],
           [1.37301685e-03, 1.36800262e-03, 1.72055651e-03],
           [6.65756539e-04, 6.60629159e-04, 8.10977578e-04],
           [1.92918273e-04, 1.90603023e-04, 2.27925431e-04],
           [0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
           [2.46147513e-04, 1.74022352e-04, 1.86778068e-04],
           [8.76505979e-04, 5.95218163e-04, 6.45816030e-04],
           [1.86026397e-03, 1.21726718e-03, 1.33402215e-03],
           [3.19002026e-03, 2.01788637e-03, 2.23163475e-03],
           [4.86438398e-03, 2.98218359e-03, 3.32571522e-03],
           [6.88465127e-03, 4.09899757e-03, 4.60663725e-03],
           [9.25360203e-03, 5.35941200e-03, 6.06669606e-03],
           [1.19749644e-02, 6.75599550e-03, 7.69941449e-03],
           [1.50531009e-02, 8.28237546e-03, 9.49915213e-03],
           [1.84928310e-02, 9.93296829e-03, 1.14608625e-02],
           [2.22993192e-02, 1.17027997e-02, 1.35799324e-02],
           [2.64780094e-02, 1.35873759e-02, 1.58520698e-02],
           [3.10345812e-02, 1.55825903e-02, 1.82732221e-02],
           [3.59748385e-02, 1.76846830e-02, 2.08395272e-02],
           [4.12852700e-02, 1.98901549e-02, 2.35472554e-02],
           [4.66368784e-02, 2.21957396e-02, 2.63927782e-02],
           [5.19582875e-02, 2.45983712e-02, 2.93725400e-02],
           [5.72533152e-02, 2.70951584e-02, 3.24830352e-02],
           [6.25252807e-02, 2.96833639e-02, 3.57207896e-02],
           [6.77770915e-02, 3.23603867e-02, 3.90823447e-02],
           [7.30113526e-02, 3.51237250e-02, 4.24978599e-02],
           [7.82303272e-02, 3.79710125e-02, 4.58514661e-02],
           [8.34360241e-02, 4.08909771e-02, 4.91545205e-02],
           [8.86302578e-02, 4.37692089e-02, 5.24087069e-02],
           [9.38146597e-02, 4.66043370e-02, 5.56155029e-02],
           [9.89907016e-02, 4.93982504e-02, 5.87762063e-02],
           [1.04159716e-01, 5.21526804e-02, 6.18919566e-02],
           [1.09323027e-01, 5.48691472e-02, 6.49637131e-02],
           [1.14481684e-01, 5.75491529e-02, 6.79923662e-02],
           [1.19636642e-01, 6.01940916e-02, 7.09786970e-02],
           [1.24788816e-01, 6.28052319e-02, 7.39233708e-02],
           [1.29939212e-01, 6.53836503e-02, 7.68268958e-02],
           [1.35088504e-01, 6.79305129e-02, 7.96897984e-02],
           [1.40237336e-01, 7.04469011e-02, 8.25125235e-02],
           [1.45386532e-01, 7.29336764e-02, 8.52953436e-02],
           [1.50536608e-01, 7.53918162e-02, 8.80385793e-02],
           [1.55688036e-01, 7.78222467e-02, 9.07424959e-02],
           [1.60841582e-01, 8.02256210e-02, 9.34071441e-02],
           [1.65997414e-01, 8.26029302e-02, 9.60327923e-02],
           [1.71156234e-01, 8.49547419e-02, 9.86193846e-02],
           [1.76318204e-01, 8.72819357e-02, 1.01167075e-01],
           [1.81483900e-01, 8.95850555e-02, 1.03675746e-01],
           [1.86653425e-01, 9.18649272e-02, 1.06145482e-01],
           [1.91827351e-01, 9.41220038e-02, 1.08576054e-01],
           [1.97005671e-01, 9.63571069e-02, 1.10967514e-01],
           [2.02188847e-01, 9.85706910e-02, 1.13319597e-01],
           [2.07376987e-01, 1.00763426e-01, 1.15632203e-01],
           [2.12570219e-01, 1.02935942e-01, 1.17905181e-01],
           [2.17768918e-01, 1.05088657e-01, 1.20138181e-01],
           [2.22973068e-01, 1.07222249e-01, 1.22331066e-01],
           [2.28182775e-01, 1.09337286e-01, 1.24483588e-01],
           [2.33398171e-01, 1.11434291e-01, 1.26595440e-01],
           [2.38619448e-01, 1.13513724e-01, 1.28666239e-01],
           [2.43846529e-01, 1.15576226e-01, 1.30695759e-01],
           [2.49079460e-01, 1.17622332e-01, 1.32683657e-01],
           [2.54318260e-01, 1.19652578e-01, 1.34629577e-01],
           [2.59562928e-01, 1.21667505e-01, 1.36533148e-01],
           [2.64813442e-01, 1.23667656e-01, 1.38393988e-01],
           [2.70069756e-01, 1.25653580e-01, 1.40211703e-01],
           [2.75331803e-01, 1.27625835e-01, 1.41985890e-01],
           [2.80599494e-01, 1.29584983e-01, 1.43716137e-01],
           [2.85872717e-01, 1.31531598e-01, 1.45402025e-01],
           [2.91151339e-01, 1.33466264e-01, 1.47043129e-01],
           [2.96435206e-01, 1.35389575e-01, 1.48639022e-01],
           [3.01724140e-01, 1.37302137e-01, 1.50189271e-01],
           [3.07017942e-01, 1.39204570e-01, 1.51693441e-01],
           [3.12316392e-01, 1.41097508e-01, 1.53151101e-01],
           [3.17619276e-01, 1.42981578e-01, 1.54561785e-01],
           [3.22926417e-01, 1.44857371e-01, 1.55924965e-01],
           [3.28237424e-01, 1.46725651e-01, 1.57240321e-01],
           [3.33551986e-01, 1.48587117e-01, 1.58507432e-01],
           [3.38869899e-01, 1.50442384e-01, 1.59725736e-01],
           [3.44190755e-01, 1.52292228e-01, 1.60894879e-01],
           [3.49514112e-01, 1.54137453e-01, 1.62014539e-01],
           [3.54839798e-01, 1.55978652e-01, 1.63084046e-01],
           [3.60167172e-01, 1.57816792e-01, 1.64103290e-01],
           [3.65495983e-01, 1.59652533e-01, 1.65071661e-01],
           [3.70825630e-01, 1.61486816e-01, 1.65988979e-01],
           [3.76155790e-01, 1.63320362e-01, 1.66854691e-01],
           [3.81485801e-01, 1.65154171e-01, 1.67668687e-01],
           [3.86815321e-01, 1.66988983e-01, 1.68430400e-01],
           [3.92143672e-01, 1.68825817e-01, 1.69139733e-01],
           [3.97470300e-01, 1.70665596e-01, 1.69796407e-01],
           [4.02794733e-01, 1.72509174e-01, 1.70400001e-01],
           [4.08116246e-01, 1.74357619e-01, 1.70950482e-01],
           [4.13434223e-01, 1.76211913e-01, 1.71447650e-01],
           [4.18748034e-01, 1.78073048e-01, 1.71891317e-01],
           [4.24057053e-01, 1.79942020e-01, 1.72281288e-01],
           [4.29360527e-01, 1.81819926e-01, 1.72617585e-01],
           [4.34657751e-01, 1.83707828e-01, 1.72900156e-01],
           [4.39947997e-01, 1.85606807e-01, 1.73128995e-01],
           [4.45230519e-01, 1.87517957e-01, 1.73304138e-01],
           [4.50504552e-01, 1.89442389e-01, 1.73425666e-01],
           [4.55769314e-01, 1.91381222e-01, 1.73493708e-01],
           [4.61024009e-01, 1.93335590e-01, 1.73508441e-01],
           [4.66267824e-01, 1.95306630e-01, 1.73470091e-01],
           [4.71499934e-01, 1.97295488e-01, 1.73378936e-01],
           [4.76719505e-01, 1.99303311e-01, 1.73235304e-01],
           [4.81925691e-01, 2.01331246e-01, 1.73039575e-01],
           [4.87117640e-01, 2.03380438e-01, 1.72792182e-01],
           [4.92294494e-01, 2.05452026e-01, 1.72493611e-01],
           [4.97455391e-01, 2.07547139e-01, 1.72144397e-01],
           [5.02599493e-01, 2.09666876e-01, 1.71745060e-01],
           [5.07725909e-01, 2.11812363e-01, 1.71296317e-01],
           [5.12833776e-01, 2.13984686e-01, 1.70798863e-01],
           [5.17922237e-01, 2.16184908e-01, 1.70253444e-01],
           [5.22990450e-01, 2.18414064e-01, 1.69660829e-01],
           [5.28037579e-01, 2.20673161e-01, 1.69021843e-01],
           [5.33062774e-01, 2.22963193e-01, 1.68337432e-01],
           [5.38065218e-01, 2.25285109e-01, 1.67608532e-01],
           [5.43044118e-01, 2.27639809e-01, 1.66836082e-01],
           [5.47998680e-01, 2.30028173e-01, 1.66021135e-01],
           [5.52928132e-01, 2.32451032e-01, 1.65164771e-01],
           [5.57831731e-01, 2.34909168e-01, 1.64268071e-01],
           [5.62708754e-01, 2.37403318e-01, 1.63332170e-01],
           [5.67558496e-01, 2.39934176e-01, 1.62358251e-01],
           [5.72380288e-01, 2.42502377e-01, 1.61347500e-01],
           [5.77173482e-01, 2.45108509e-01, 1.60301144e-01],
           [5.81937464e-01, 2.47753104e-01, 1.59220422e-01],
           [5.86671648e-01, 2.50436641e-01, 1.58106593e-01],
           [5.91375476e-01, 2.53159547e-01, 1.56960963e-01],
           [5.96048431e-01, 2.55922186e-01, 1.55784795e-01],
           [6.00690025e-01, 2.58724872e-01, 1.54579383e-01],
           [6.05299795e-01, 2.61567868e-01, 1.53346096e-01],
           [6.09877327e-01, 2.64451374e-01, 1.52086202e-01],
           [6.14422235e-01, 2.67375541e-01, 1.50801006e-01],
           [6.18934164e-01, 2.70340469e-01, 1.49491852e-01],
           [6.23412791e-01, 2.73346205e-01, 1.48160097e-01],
           [6.27857838e-01, 2.76392746e-01, 1.46806994e-01],
           [6.32269052e-01, 2.79480042e-01, 1.45433849e-01],
           [6.36646215e-01, 2.82607999e-01, 1.44041966e-01],
           [6.40989134e-01, 2.85776477e-01, 1.42632739e-01],
           [6.45297659e-01, 2.88985295e-01, 1.41207377e-01],
           [6.49571664e-01, 2.92234234e-01, 1.39767157e-01],
           [6.53811053e-01, 2.95523039e-01, 1.38313357e-01],
           [6.58015758e-01, 2.98851420e-01, 1.36847250e-01],
           [6.62185738e-01, 3.02219054e-01, 1.35370102e-01],
           [6.66320976e-01, 3.05625592e-01, 1.33883177e-01],
           [6.70421484e-01, 3.09070655e-01, 1.32387733e-01],
           [6.74487293e-01, 3.12553842e-01, 1.30885027e-01],
           [6.78518458e-01, 3.16074730e-01, 1.29376316e-01],
           [6.82515054e-01, 3.19632876e-01, 1.27862855e-01],
           [6.86477175e-01, 3.23227823e-01, 1.26345906e-01],
           [6.90404935e-01, 3.26859097e-01, 1.24826734e-01],
           [6.94298461e-01, 3.30526213e-01, 1.23306613e-01],
           [6.98157897e-01, 3.34228678e-01, 1.21786827e-01],
           [7.01983399e-01, 3.37965989e-01, 1.20268676e-01],
           [7.05775137e-01, 3.41737638e-01, 1.18753475e-01],
           [7.09533310e-01, 3.45543087e-01, 1.17242773e-01],
           [7.13258104e-01, 3.49381833e-01, 1.15737837e-01],
           [7.16949709e-01, 3.53253370e-01, 1.14239993e-01],
           [7.20608339e-01, 3.57157179e-01, 1.12750718e-01],
           [7.24234250e-01, 3.61092692e-01, 1.11271837e-01],
           [7.27827621e-01, 3.65059457e-01, 1.09804493e-01],
           [7.31388705e-01, 3.69056933e-01, 1.08350482e-01],
           [7.34917753e-01, 3.73084598e-01, 1.06911544e-01],
           [7.38414962e-01, 3.77141999e-01, 1.05489118e-01],
           [7.41880648e-01, 3.81228563e-01, 1.04085438e-01],
           [7.45314977e-01, 3.85343889e-01, 1.02701856e-01],
           [7.48718277e-01, 3.89487412e-01, 1.01340774e-01],
           [7.52090741e-01, 3.93658724e-01, 1.00003836e-01],
           [7.55432637e-01, 3.97857342e-01, 9.86932340e-02],
           [7.58744257e-01, 4.02082772e-01, 9.74113263e-02],
           [7.62025784e-01, 4.06334640e-01, 9.61599910e-02],
           [7.65277515e-01, 4.10612466e-01, 9.49417866e-02],
           [7.68499734e-01, 4.14915794e-01, 9.37592638e-02],
           [7.71692631e-01, 4.19244269e-01, 9.26146231e-02],
           [7.74856461e-01, 4.23597480e-01, 9.15104700e-02],
           [7.77991478e-01, 4.27975026e-01, 9.04494842e-02],
           [7.81097999e-01, 4.32376459e-01, 8.94346788e-02],
           [7.84176206e-01, 4.36801463e-01, 8.84685728e-02],
           [7.87226341e-01, 4.41249676e-01, 8.75540097e-02],
           [7.90248648e-01, 4.45720742e-01, 8.66938986e-02],
           [7.93243365e-01, 4.50214316e-01, 8.58911823e-02],
           [7.96210730e-01, 4.54730066e-01, 8.51488247e-02],
           [7.99150975e-01, 4.59267669e-01, 8.44697961e-02],
           [8.02064329e-01, 4.63826814e-01, 8.38570574e-02],
           [8.04951015e-01, 4.68407202e-01, 8.33135422e-02],
           [8.07811252e-01, 4.73008544e-01, 8.28421385e-02],
           [8.10645255e-01, 4.77630563e-01, 8.24456683e-02],
           [8.13453293e-01, 4.82272944e-01, 8.21270520e-02],
           [8.16235580e-01, 4.86935423e-01, 8.18889382e-02],
           [8.18992270e-01, 4.91617793e-01, 8.17336794e-02],
           [8.21723559e-01, 4.96319820e-01, 8.16636252e-02],
           [8.24429634e-01, 5.01041277e-01, 8.16809565e-02],
           [8.27110882e-01, 5.05781794e-01, 8.17882158e-02],
           [8.29767327e-01, 5.10541287e-01, 8.19867447e-02],
           [8.32399121e-01, 5.15319577e-01, 8.22780547e-02],
           [8.35006656e-01, 5.20116310e-01, 8.26640340e-02],
           [8.37589979e-01, 5.24931398e-01, 8.31454551e-02],
           [8.40149219e-01, 5.29764695e-01, 8.37230852e-02],
           [8.42684814e-01, 5.34615834e-01, 8.43981411e-02],
           [8.45196602e-01, 5.39484893e-01, 8.51702373e-02],
           [8.47685129e-01, 5.44371438e-01, 8.60403002e-02],
           [8.50150204e-01, 5.49275574e-01, 8.70074521e-02],
           [8.52592360e-01, 5.54196890e-01, 8.80720629e-02],
           [8.55011374e-01, 5.59135521e-01, 8.92327980e-02],
           [8.57407880e-01, 5.64090997e-01, 9.04897298e-02],
           [8.59781612e-01, 5.69063487e-01, 9.18410925e-02],
           [8.62132991e-01, 5.74052684e-01, 9.32861675e-02],
           [8.64462123e-01, 5.79058503e-01, 9.48235248e-02],
           [8.66769006e-01, 5.84080937e-01, 9.64514470e-02],
           [8.69054105e-01, 5.89119666e-01, 9.81687919e-02],
           [8.71317373e-01, 5.94174723e-01, 9.99735453e-02],
           [8.73558893e-01, 5.99246049e-01, 1.01863830e-01],
           [8.75778943e-01, 6.04333465e-01, 1.03837949e-01],
           [8.77977766e-01, 6.09436823e-01, 1.05894083e-01],
           [8.80155313e-01, 6.14556159e-01, 1.08030036e-01],
           [8.82311743e-01, 6.19691387e-01, 1.10243848e-01],
           [8.84447208e-01, 6.24842421e-01, 1.12533541e-01],
           [8.86561983e-01, 6.30009105e-01, 1.14897254e-01],
           [8.88656165e-01, 6.35191401e-01, 1.17332953e-01],
           [8.90729806e-01, 6.40389298e-01, 1.19838596e-01],
           [8.92783048e-01, 6.45602733e-01, 1.22412261e-01],
           [8.94816027e-01, 6.50831649e-01, 1.25052057e-01],
           [8.96828879e-01, 6.56075994e-01, 1.27756136e-01],
           [8.98821736e-01, 6.61335720e-01, 1.30522692e-01],
           [9.00794725e-01, 6.66610785e-01, 1.33349970e-01],
           [9.02747973e-01, 6.71901150e-01, 1.36236264e-01],
           [9.04681602e-01, 6.77206783e-01, 1.39179925e-01],
           [9.06595729e-01, 6.82527656e-01, 1.42179360e-01],
           [9.08490471e-01, 6.87863744e-01, 1.45233030e-01],
           [9.10365937e-01, 6.93215029e-01, 1.48339456e-01],
           [9.12222237e-01, 6.98581497e-01, 1.51497216e-01],
           [9.14059474e-01, 7.03963136e-01, 1.54704945e-01],
           [9.15877749e-01, 7.09359942e-01, 1.57961334e-01],
           [9.17677158e-01, 7.14771913e-01, 1.61265130e-01],
           [9.19457794e-01, 7.20199053e-01, 1.64615135e-01],
           [9.21219887e-01, 7.25641293e-01, 1.68010245e-01],
           [9.22963546e-01, 7.31098632e-01, 1.71449361e-01],
           [9.24688722e-01, 7.36571158e-01, 1.74931397e-01],
           [9.26395493e-01, 7.42058890e-01, 1.78455353e-01],
           [9.28083929e-01, 7.47561853e-01, 1.82020279e-01],
           [9.29754237e-01, 7.53080003e-01, 1.85625294e-01],
           [9.31406685e-01, 7.58613271e-01, 1.89269561e-01],
           [9.33041031e-01, 7.64161849e-01, 1.92952193e-01],
           [9.34657330e-01, 7.69725777e-01, 1.96672407e-01],
           [9.36255901e-01, 7.75304965e-01, 2.00429488e-01],
           [9.37836877e-01, 7.80899421e-01, 2.04222720e-01],
           [9.39399985e-01, 7.86509354e-01, 2.08051387e-01],
           [9.40945427e-01, 7.92134740e-01, 2.11914857e-01],
           [9.42473642e-01, 7.97775442e-01, 2.15812532e-01],
           [9.43984129e-01, 8.03431784e-01, 2.19743786e-01],
           [9.45477230e-01, 8.09103677e-01, 2.23708074e-01],
           [9.46953174e-01, 8.14791098e-01, 2.27704861e-01],
           [9.48411483e-01, 8.20494354e-01, 2.31733624e-01],
           [9.49852929e-01, 8.26213166e-01, 2.35793883e-01],
           [9.51276961e-01, 8.31947880e-01, 2.39885169e-01],
           [9.52683858e-01, 8.37698450e-01, 2.44007037e-01],
           [9.54073766e-01, 8.43464899e-01, 2.48159058e-01],
           [9.55446349e-01, 8.49247470e-01, 2.52340842e-01],
           [9.56802246e-01, 8.55045963e-01, 2.56551973e-01],
           [9.58140717e-01, 8.60860804e-01, 2.60792124e-01],
           [9.59462672e-01, 8.66691679e-01, 2.65060887e-01],
           [9.60767194e-01, 8.72539089e-01, 2.69357991e-01]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.iceburn", N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
