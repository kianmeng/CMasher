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
           [2.26276605e-04, 1.27312718e-04, 1.80411323e-04],
           [8.13645546e-04, 4.28891491e-04, 6.39834919e-04],
           [1.74260184e-03, 8.63685259e-04, 1.35487268e-03],
           [3.01237471e-03, 1.41020371e-03, 2.32124316e-03],
           [4.62644578e-03, 2.05319508e-03, 3.54022725e-03],
           [6.59022229e-03, 2.78050385e-03, 5.01612876e-03],
           [8.90954870e-03, 3.58208100e-03, 6.75497888e-03],
           [1.15908560e-02, 4.44910184e-03, 8.76435018e-03],
           [1.46413908e-02, 5.37339649e-03, 1.10533959e-02],
           [1.80675978e-02, 6.34788166e-03, 1.36318649e-02],
           [2.18766340e-02, 7.36569349e-03, 1.65109504e-02],
           [2.60757165e-02, 8.42034129e-03, 1.97029401e-02],
           [3.06714488e-02, 9.50591564e-03, 2.32207803e-02],
           [3.56714051e-02, 1.06162932e-02, 2.70791788e-02],
           [4.10685016e-02, 1.17460710e-02, 3.12931556e-02],
           [4.65285211e-02, 1.28895898e-02, 3.58795272e-02],
           [5.19623992e-02, 1.40414219e-02, 4.08481551e-02],
           [5.73725657e-02, 1.51965674e-02, 4.59230286e-02],
           [6.27621826e-02, 1.63494237e-02, 5.10293953e-02],
           [6.81330369e-02, 1.74950091e-02, 5.61721676e-02],
           [7.34866739e-02, 1.86283781e-02, 6.13560706e-02],
           [7.88246360e-02, 1.97444393e-02, 6.65859302e-02],
           [8.41481990e-02, 2.08381282e-02, 7.18664189e-02],
           [8.94585856e-02, 2.19042363e-02, 7.72023166e-02],
           [9.47563555e-02, 2.29379567e-02, 8.25977765e-02],
           [1.00042052e-01, 2.39343733e-02, 8.80570739e-02],
           [1.05316089e-01, 2.48885467e-02, 9.35844918e-02],
           [1.10578791e-01, 2.57954689e-02, 9.91843886e-02],
           [1.15830405e-01, 2.66500344e-02, 1.04861240e-01],
           [1.21070636e-01, 2.74476067e-02, 1.10618951e-01],
           [1.26299179e-01, 2.81834467e-02, 1.16461601e-01],
           [1.31515560e-01, 2.88529100e-02, 1.22393213e-01],
           [1.36719884e-01, 2.94503632e-02, 1.28419043e-01],
           [1.41910804e-01, 2.99720524e-02, 1.34542190e-01],
           [1.47087679e-01, 3.04131133e-02, 1.40767177e-01],
           [1.52249518e-01, 3.07690478e-02, 1.47098213e-01],
           [1.57395119e-01, 3.10355639e-02, 1.53539405e-01],
           [1.62522770e-01, 3.12091760e-02, 1.60094125e-01],
           [1.67631454e-01, 3.12849946e-02, 1.66767503e-01],
           [1.72718985e-01, 3.12602060e-02, 1.73562572e-01],
           [1.77783306e-01, 3.11317439e-02, 1.80482912e-01],
           [1.82822192e-01, 3.08968391e-02, 1.87532072e-01],
           [1.87833129e-01, 3.05533245e-02, 1.94713278e-01],
           [1.92813300e-01, 3.00997480e-02, 2.02029372e-01],
           [1.97759572e-01, 2.95354990e-02, 2.09482732e-01],
           [2.02668562e-01, 2.88607301e-02, 2.17075424e-01],
           [2.07536822e-01, 2.80758479e-02, 2.24809818e-01],
           [2.12359835e-01, 2.71846158e-02, 2.32685372e-01],
           [2.17133534e-01, 2.61897980e-02, 2.40703356e-01],
           [2.21852819e-01, 2.50978666e-02, 2.48861965e-01],
           [2.26512923e-01, 2.39146740e-02, 2.57161011e-01],
           [2.31107960e-01, 2.26507259e-02, 2.65596478e-01],
           [2.35632053e-01, 2.13174337e-02, 2.74164607e-01],
           [2.40078898e-01, 1.99288965e-02, 2.82860163e-01],
           [2.44441782e-01, 1.85021500e-02, 2.91676310e-01],
           [2.48713619e-01, 1.70573983e-02, 3.00604515e-01],
           [2.52886990e-01, 1.56182158e-02, 3.09634466e-01],
           [2.56954197e-01, 1.42117103e-02, 3.18754028e-01],
           [2.60907438e-01, 1.28676949e-02, 3.27950264e-01],
           [2.64738513e-01, 1.16214214e-02, 3.37206528e-01],
           [2.68439333e-01, 1.05104322e-02, 3.46505955e-01],
           [2.72001719e-01, 9.57681225e-03, 3.55828951e-01],
           [2.75417682e-01, 8.86512879e-03, 3.65155462e-01],
           [2.78679382e-01, 8.42414452e-03, 3.74462817e-01],
           [2.81779365e-01, 8.30465889e-03, 3.83728003e-01],
           [2.84710616e-01, 8.55960989e-03, 3.92927234e-01],
           [2.87466680e-01, 9.24360942e-03, 4.02036057e-01],
           [2.90041783e-01, 1.04120726e-02, 4.11029880e-01],
           [2.92430908e-01, 1.21202905e-02, 4.19884539e-01],
           [2.94629881e-01, 1.44227121e-02, 4.28576550e-01],
           [2.96635430e-01, 1.73721113e-02, 4.37083472e-01],
           [2.98445227e-01, 2.10187836e-02, 4.45384250e-01],
           [3.00057912e-01, 2.54098035e-02, 4.53459503e-01],
           [3.01473093e-01, 3.05883652e-02, 4.61291770e-01],
           [3.02691333e-01, 3.65932275e-02, 4.68865688e-01],
           [3.03714113e-01, 4.33459818e-02, 4.76168119e-01],
           [3.04543788e-01, 5.03089764e-02, 4.83188214e-01],
           [3.05183552e-01, 5.73972054e-02, 4.89917380e-01],
           [3.05637357e-01, 6.45786844e-02, 4.96349292e-01],
           [3.05909774e-01, 7.18266691e-02, 5.02479894e-01],
           [3.06005992e-01, 7.91185312e-02, 5.08307152e-01],
           [3.05931720e-01, 8.64349607e-02, 5.13830946e-01],
           [3.05693350e-01, 9.37591547e-02, 5.19052743e-01],
           [3.05297195e-01, 1.01076990e-01, 5.23975987e-01],
           [3.04750235e-01, 1.08375946e-01, 5.28605241e-01],
           [3.04059596e-01, 1.15645248e-01, 5.32946397e-01],
           [3.03232492e-01, 1.22875650e-01, 5.37006449e-01],
           [3.02276329e-01, 1.30059116e-01, 5.40793256e-01],
           [3.01198730e-01, 1.37188614e-01, 5.44315400e-01],
           [3.00006926e-01, 1.44258482e-01, 5.47582132e-01],
           [2.98708466e-01, 1.51263666e-01, 5.50603094e-01],
           [2.97311060e-01, 1.58199751e-01, 5.53388297e-01],
           [2.95821763e-01, 1.65063524e-01, 5.55947986e-01],
           [2.94247830e-01, 1.71852165e-01, 5.58292520e-01],
           [2.92596376e-01, 1.78563447e-01, 5.60432310e-01],
           [2.90874351e-01, 1.85195677e-01, 5.62377737e-01],
           [2.89088529e-01, 1.91747644e-01, 5.64139085e-01],
           [2.87245485e-01, 1.98218563e-01, 5.65726484e-01],
           [2.85351594e-01, 2.04608035e-01, 5.67149861e-01],
           [2.83413456e-01, 2.10915702e-01, 5.68419067e-01],
           [2.81436722e-01, 2.17142018e-01, 5.69543432e-01],
           [2.79427085e-01, 2.23287509e-01, 5.70532063e-01],
           [2.77390446e-01, 2.29352664e-01, 5.71393943e-01],
           [2.75332194e-01, 2.35338370e-01, 5.72137624e-01],
           [2.73257117e-01, 2.41245918e-01, 5.72771129e-01],
           [2.71170901e-01, 2.47076083e-01, 5.73302701e-01],
           [2.69077524e-01, 2.52830653e-01, 5.73739488e-01],
           [2.66982204e-01, 2.58510682e-01, 5.74089063e-01],
           [2.64888879e-01, 2.64117927e-01, 5.74358093e-01],
           [2.62801535e-01, 2.69654066e-01, 5.74553043e-01],
           [2.60724846e-01, 2.75120374e-01, 5.74680596e-01],
           [2.58661851e-01, 2.80518926e-01, 5.74746273e-01],
           [2.56616122e-01, 2.85851443e-01, 5.74755724e-01],
           [2.54591014e-01, 2.91119686e-01, 5.74714297e-01],
           [2.52589881e-01, 2.96325342e-01, 5.74627193e-01],
           [2.50615459e-01, 3.01470315e-01, 5.74499066e-01],
           [2.48670327e-01, 3.06556485e-01, 5.74334333e-01],
           [2.46756966e-01, 3.11585683e-01, 5.74137222e-01],
           [2.44877634e-01, 3.16559747e-01, 5.73911702e-01],
           [2.43034370e-01, 3.21480509e-01, 5.73661496e-01],
           [2.41228992e-01, 3.26349796e-01, 5.73390091e-01],
           [2.39463093e-01, 3.31169427e-01, 5.73100744e-01],
           [2.37738045e-01, 3.35941206e-01, 5.72796490e-01],
           [2.36055089e-01, 3.40666885e-01, 5.72480223e-01],
           [2.34415313e-01, 3.45348176e-01, 5.72154692e-01],
           [2.32819208e-01, 3.49986913e-01, 5.71822172e-01],
           [2.31267247e-01, 3.54584828e-01, 5.71484901e-01],
           [2.29759674e-01, 3.59143632e-01, 5.71144938e-01],
           [2.28296744e-01, 3.63664926e-01, 5.70804345e-01],
           [2.26878372e-01, 3.68150337e-01, 5.70464933e-01],
           [2.25503818e-01, 3.72601615e-01, 5.70128014e-01],
           [2.24172534e-01, 3.77020340e-01, 5.69795062e-01],
           [2.22884153e-01, 3.81407933e-01, 5.69467716e-01],
           [2.21637028e-01, 3.85766151e-01, 5.69146629e-01],
           [2.20430218e-01, 3.90096415e-01, 5.68833034e-01],
           [2.19262307e-01, 3.94400211e-01, 5.68527815e-01],
           [2.18131274e-01, 3.98679129e-01, 5.68231398e-01],
           [2.17035891e-01, 4.02934418e-01, 5.67944860e-01],
           [2.15973349e-01, 4.07167737e-01, 5.67668048e-01],
           [2.14942228e-01, 4.11380235e-01, 5.67401924e-01],
           [2.13939308e-01, 4.15573526e-01, 5.67146035e-01],
           [2.12962851e-01, 4.19748706e-01, 5.66901114e-01],
           [2.12009369e-01, 4.23907314e-01, 5.66666509e-01],
           [2.11076653e-01, 4.28050447e-01, 5.66442575e-01],
           [2.10161233e-01, 4.32179499e-01, 5.66228665e-01],
           [2.09260221e-01, 4.36295630e-01, 5.66024572e-01],
           [2.08370440e-01, 4.40400029e-01, 5.65829838e-01],
           [2.07488259e-01, 4.44493944e-01, 5.65643622e-01],
           [2.06610787e-01, 4.48578377e-01, 5.65465614e-01],
           [2.05734127e-01, 4.52654541e-01, 5.65294683e-01],
           [2.04854699e-01, 4.56723519e-01, 5.65129893e-01],
           [2.03969407e-01, 4.60786226e-01, 5.64970605e-01],
           [2.03074154e-01, 4.64843787e-01, 5.64815361e-01],
           [2.02165314e-01, 4.68897167e-01, 5.64662985e-01],
           [2.01239556e-01, 4.72947222e-01, 5.64512433e-01],
           [2.00293005e-01, 4.76994905e-01, 5.64362175e-01],
           [1.99321941e-01, 4.81041095e-01, 5.64210707e-01],
           [1.98322790e-01, 4.85086604e-01, 5.64056530e-01],
           [1.97292251e-01, 4.89132157e-01, 5.63898240e-01],
           [1.96226488e-01, 4.93178565e-01, 5.63733952e-01],
           [1.95122039e-01, 4.97226530e-01, 5.63561938e-01],
           [1.93975507e-01, 5.01276713e-01, 5.63380408e-01],
           [1.92783762e-01, 5.05329695e-01, 5.63187639e-01],
           [1.91543423e-01, 5.09386085e-01, 5.62981631e-01],
           [1.90251290e-01, 5.13446432e-01, 5.62760393e-01],
           [1.88904330e-01, 5.17511230e-01, 5.62521937e-01],
           [1.87499622e-01, 5.21580929e-01, 5.62264235e-01],
           [1.86034475e-01, 5.25655916e-01, 5.61985292e-01],
           [1.84506168e-01, 5.29736567e-01, 5.61682987e-01],
           [1.82912094e-01, 5.33823219e-01, 5.61355165e-01],
           [1.81249866e-01, 5.37916149e-01, 5.60999697e-01],
           [1.79517253e-01, 5.42015597e-01, 5.60614444e-01],
           [1.77712186e-01, 5.46121756e-01, 5.60197260e-01],
           [1.75832802e-01, 5.50234776e-01, 5.59746014e-01],
           [1.73877415e-01, 5.54354766e-01, 5.59258573e-01],
           [1.71844426e-01, 5.58481812e-01, 5.58732749e-01],
           [1.69732520e-01, 5.62615948e-01, 5.58166407e-01],
           [1.67540603e-01, 5.66757169e-01, 5.57557431e-01],
           [1.65267818e-01, 5.70905435e-01, 5.56903717e-01],
           [1.62913562e-01, 5.75060667e-01, 5.56203186e-01],
           [1.60477508e-01, 5.79222751e-01, 5.55453779e-01],
           [1.57959653e-01, 5.83391536e-01, 5.54653475e-01],
           [1.55360265e-01, 5.87566847e-01, 5.53800255e-01],
           [1.52680010e-01, 5.91748471e-01, 5.52892142e-01],
           [1.49919961e-01, 5.95936164e-01, 5.51927197e-01],
           [1.47081648e-01, 6.00129652e-01, 5.50903517e-01],
           [1.44167107e-01, 6.04328632e-01, 5.49819231e-01],
           [1.41178951e-01, 6.08532774e-01, 5.48672507e-01],
           [1.38120444e-01, 6.12741721e-01, 5.47461551e-01],
           [1.34995517e-01, 6.16955100e-01, 5.46184565e-01],
           [1.31809058e-01, 6.21172500e-01, 5.44839848e-01],
           [1.28566907e-01, 6.25393490e-01, 5.43425723e-01],
           [1.25276014e-01, 6.29617616e-01, 5.41940545e-01],
           [1.21944616e-01, 6.33844406e-01, 5.40382708e-01],
           [1.18582433e-01, 6.38073361e-01, 5.38750642e-01],
           [1.15200891e-01, 6.42303968e-01, 5.37042815e-01],
           [1.11813153e-01, 6.46535711e-01, 5.35257624e-01],
           [1.08434919e-01, 6.50768024e-01, 5.33393648e-01],
           [1.05084411e-01, 6.55000329e-01, 5.31449486e-01],
           [1.01782647e-01, 6.59232033e-01, 5.29423739e-01],
           [9.85538432e-02, 6.63462527e-01, 5.27315039e-01],
           [9.54257237e-02, 6.67691180e-01, 5.25122046e-01],
           [9.24291756e-02, 6.71917396e-01, 5.22843158e-01],
           [8.96001472e-02, 6.76140468e-01, 5.20477332e-01],
           [8.69780422e-02, 6.80359713e-01, 5.18023307e-01],
           [8.46060155e-02, 6.84574429e-01, 5.15479849e-01],
           [8.25301048e-02, 6.88783922e-01, 5.12845567e-01],
           [8.07987492e-02, 6.92987473e-01, 5.10119108e-01],
           [7.94622344e-02, 6.97184282e-01, 5.07299570e-01],
           [7.85695703e-02, 7.01373568e-01, 5.04385805e-01],
           [7.81662260e-02, 7.05554580e-01, 5.01376261e-01],
           [7.82934535e-02, 7.09726484e-01, 4.98269870e-01],
           [7.89855453e-02, 7.13888391e-01, 4.95065822e-01],
           [8.02667144e-02, 7.18039468e-01, 4.91762664e-01],
           [8.21511806e-02, 7.22178843e-01, 4.88359025e-01],
           [8.46436738e-02, 7.26305515e-01, 4.84854450e-01],
           [8.77372925e-02, 7.30418604e-01, 4.81247108e-01],
           [9.14175290e-02, 7.34517083e-01, 4.77536213e-01],
           [9.56626722e-02, 7.38599901e-01, 4.73720978e-01],
           [1.00445183e-01, 7.42666076e-01, 4.69799360e-01],
           [1.05735811e-01, 7.46714388e-01, 4.65771688e-01],
           [1.11502467e-01, 7.50743825e-01, 4.61635123e-01],
           [1.17714552e-01, 7.54753046e-01, 4.57390561e-01],
           [1.24341602e-01, 7.58740931e-01, 4.53035113e-01],
           [1.31355713e-01, 7.62706066e-01, 4.48569410e-01],
           [1.38731060e-01, 7.66647140e-01, 4.43991600e-01],
           [1.46444562e-01, 7.70562706e-01, 4.39300895e-01],
           [1.54475605e-01, 7.74451215e-01, 4.34497312e-01],
           [1.62806583e-01, 7.78311121e-01, 4.29579088e-01],
           [1.71422174e-01, 7.82140724e-01, 4.24545929e-01],
           [1.80309215e-01, 7.85938227e-01, 4.19397985e-01],
           [1.89456914e-01, 7.89701749e-01, 4.14134933e-01],
           [1.98856493e-01, 7.93429292e-01, 4.08756702e-01],
           [2.08501001e-01, 7.97118723e-01, 4.03263535e-01],
           [2.18385197e-01, 8.00767770e-01, 3.97655978e-01],
           [2.28505055e-01, 8.04374001e-01, 3.91935528e-01],
           [2.38858250e-01, 8.07934818e-01, 3.86103684e-01],
           [2.49443357e-01, 8.11447438e-01, 3.80163200e-01],
           [2.60260024e-01, 8.14908884e-01, 3.74117745e-01],
           [2.71308758e-01, 8.18315970e-01, 3.67972260e-01],
           [2.82590964e-01, 8.21665281e-01, 3.61733008e-01],
           [2.94110727e-01, 8.24953047e-01, 3.55405559e-01],
           [3.05868369e-01, 8.28175462e-01, 3.49003188e-01],
           [3.17869729e-01, 8.31328156e-01, 3.42535504e-01],
           [3.30115919e-01, 8.34406799e-01, 3.36021381e-01],
           [3.42611750e-01, 8.37406533e-01, 3.29479311e-01],
           [3.55360109e-01, 8.40322355e-01, 3.22934571e-01],
           [3.68362036e-01, 8.43149163e-01, 3.16419472e-01],
           [3.81617776e-01, 8.45881692e-01, 3.09972790e-01],
           [3.95124842e-01, 8.48514754e-01, 3.03642336e-01],
           [4.08877490e-01, 8.51043391e-01, 2.97485829e-01],
           [4.22865811e-01, 8.53463107e-01, 2.91571898e-01],
           [4.37070912e-01, 8.55770710e-01, 2.85983739e-01],
           [4.51469752e-01, 8.57963958e-01, 2.80813591e-01],
           [4.66027126e-01, 8.60043018e-01, 2.76166797e-01]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.lavender", N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
