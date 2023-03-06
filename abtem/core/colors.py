from matplotlib.colors import ListedColormap

hsluv = [(0.9677975592919913, 0.44127456009157356, 0.5358103155058701),
         (0.9679905686247109, 0.4427086936525099, 0.5232471902345959),
         (0.9681846833909024, 0.4441456091807078, 0.5102108920317392),
         (0.9683801479435378, 0.44558707166385464, 0.496640462931676),
         (0.9685772133084095, 0.4470348684220113, 0.48246466891236545),
         (0.9687761385142649, 0.4484908181272162, 0.4675992808892698),
         (0.9689771920092721, 0.44995678015687207, 0.451943373633412),
         (0.9691806531808481, 0.45143466438557317, 0.4353741684844139),
         (0.9693868139978655, 0.4529264415282586, 0.4177396490314462),
         (0.9695959807966686, 0.45443415415809923, 0.3988476449777347),
         (0.9698084762352132, 0.4559599285356711, 0.378449067362264),
         (0.9700246414431443, 0.4575059874020944, 0.35621093685538846),
         (0.9702448383998029, 0.4590746639084818, 0.331670401478718),
         (0.9704694525771783, 0.4606684168778192, 0.3041502779735699),
         (0.9706988958908692, 0.4622898476241309, 0.2725876204802891),
         (0.9709336100093858, 0.4639417185883978, 0.2351325645868269),
         (0.9688417625390765, 0.46710871459052145, 0.1965441952393453),
         (0.9551738774671777, 0.47730690217492816, 0.19640093754314353),
         (0.942248507764417, 0.4865360803194693, 0.1962678332937705),
         (0.9299877343983209, 0.49494338885920924, 0.19614369630055),
         (0.9183238180591338, 0.5026469537693952, 0.19602751520611572),
         (0.9071975303984048, 0.5097428969577137, 0.1959184222473579),
         (0.8965568047488394, 0.5163103629891463, 0.19581566847548237),
         (0.8863556363832769, 0.5224152001083757, 0.1957186039283711),
         (0.8765531794402894, 0.5281127054203663, 0.19562666163714132),
         (0.8671130001393752, 0.533449705224052, 0.19553934462828082),
         (0.8580024551580084, 0.5384661540786425, 0.19545621528593832),
         (0.8491921709604139, 0.5431963796502367, 0.19537688658847108),
         (0.8406556050916162, 0.5476700629467893, 0.1953010148442934),
         (0.8323686744304558, 0.5519130182238807, 0.1952282936354366),
         (0.8243094384533829, 0.5559478193849938, 0.19515844874018),
         (0.8164578279290011, 0.5597943074573427, 0.19509123385428534),
         (0.8087954113106306, 0.5634700050056693, 0.19502642696727285),
         (0.8013051925449828, 0.5669904570495057, 0.1949638272789701),
         (0.7939714351617072, 0.5703695134426877, 0.19490325256382088),
         (0.7867795084201196, 0.5736195642636965, 0.19484453690815204),
         (0.7797157520179037, 0.5767517372133368, 0.1947875287593524),
         (0.7727673564515078, 0.579776064087089, 0.19473208923713442),
         (0.765922256589548, 0.5827016219175047, 0.19467809066575562),
         (0.7591690364019644, 0.5855366532491194, 0.19462541529327362),
         (0.7524968430969101, 0.5882886691293608, 0.19457395416960102),
         (0.7458953091682919, 0.5909645377117685, 0.19452360615983835),
         (0.7393544810603669, 0.5935705608268428, 0.19447427707312873),
         (0.7328647533202635, 0.59611254044711, 0.1944258788904054),
         (0.7264168072413041, 0.5985958366311214, 0.1943783290769844),
         (0.7200015531046753, 0.6010254182569204, 0.19433154996803736),
         (0.7136100752081747, 0.6034059076344453, 0.19428546821673415),
         (0.7072335789314197, 0.6057416199071816, 0.19424001429632337),
         (0.7008633391290917, 0.6080365980075504, 0.19419512204856468),
         (0.6944906491688961, 0.6102946438113089, 0.194150728272025),
         (0.6881067699396747, 0.6125193460384235, 0.19410677234446388),
         (0.6817028781475658, 0.6147141053673759, 0.1940631958743251),
         (0.6752700131937613, 0.6168821571634282, 0.19401994237692713),
         (0.6687990218850333, 0.6190265921664487, 0.1939769569713208),
         (0.6622805001657721, 0.6211503754384625, 0.19393418609432778),
         (0.655704730974966, 0.6232563638334994, 0.19389157722846465),
         (0.6490616172193203, 0.6253473222212846, 0.19384907864075884),
         (0.6423406087092329, 0.6274259386708158, 0.19380663912970322),
         (0.6355306217204847, 0.6294948387790598, 0.19376420777763845),
         (0.628619949611822, 0.6315565993132425, 0.19372173370607063),
         (0.6215961626346623, 0.6336137613219601, 0.19367916583134742),
         (0.6144459946993567, 0.635668842860234, 0.1936364526182892),
         (0.6071552143907416, 0.6377243514663377, 0.19359354182914107),
         (0.599708476924399, 0.6397827965235551, 0.19355038026531127),
         (0.5920891529639701, 0.6418467016378244, 0.1935069134991043),
         (0.5842791292240528, 0.643918617162435, 0.19346308559254877),
         (0.5762585744868047, 0.6460011330035635, 0.19341883880014535),
         (0.5680056629573976, 0.6480968918455491, 0.1933741132520979),
         (0.5594962446241074, 0.6502086029425318, 0.19332884661418084),
         (0.5507034492584356, 0.6523390566336771, 0.1932829737199967),
         (0.5415972065774083, 0.6544911397529312, 0.1932364261707768),
         (0.5321436594336149, 0.656667852121568, 0.19318913189728346),
         (0.522304439007494, 0.6588723243331578, 0.19314101467753325),
         (0.5120357597934629, 0.6611078370667207, 0.1930919936031362),
         (0.5012872760462653, 0.6633778421955273, 0.19304198248590768),
         (0.49000061765110564, 0.6656859859973139, 0.19299088919506124),
         (0.47810748778716866, 0.6680361348178981, 0.19293861491359926),
         (0.46552715000937533, 0.6704324035959093, 0.19288505330057484),
         (0.4521630458730797, 0.6728791877236074, 0.19283008954347472),
         (0.43789814330136734, 0.6753811988001035, 0.19277359928204552),
         (0.4225883781014591, 0.677943504931845, 0.19271544738133076),
         (0.40605313314369507, 0.6805715763550605, 0.19265548652729286),
         (0.388060929443388, 0.6832713373010088, 0.1925935556130633),
         (0.368307000568552, 0.6860492252038582, 0.19252947787719096),
         (0.346376280235058, 0.6889122585711249, 0.19246305874702868),
         (0.32167817651263064, 0.6918681151085289, 0.19239408333012523),
         (0.293321299642657, 0.69492522202874, 0.19232231348356066),
         (0.259842565108932, 0.6980928608948738, 0.19224748437488157),
         (0.21850838711193937, 0.7013812898784881, 0.19216930042759509),
         (0.19263252512500093, 0.7025502327896916, 0.21697163648510331),
         (0.19351548852774433, 0.7013832753217172, 0.25858958069296223),
         (0.1943431993979385, 0.7002817475077833, 0.29172995496049464),
         (0.19512161067678968, 0.6992390765358367, 0.31940698844992155),
         (0.19585587013733535, 0.6982495089895844, 0.3432132996634462),
         (0.19655045355310197, 0.6973079851810643, 0.36411157917293036),
         (0.19720927229668667, 0.696410035834187, 0.3827359968385837),
         (0.19783576093349015, 0.6955516966063037, 0.3995301037444499),
         (0.1984329490312679, 0.6947294369468084, 0.41481814266762784),
         (0.1990035204169881, 0.6939401005552839, 0.4288453245948835),
         (0.1995498623771409, 0.6931808552827505, 0.4418021507065804),
         (0.200074106745598, 0.6924491507653744, 0.4538398923952646),
         (0.20057816440502163, 0.6917426824246335, 0.46508087066632137),
         (0.20106375440834434, 0.6910593607362929, 0.4756255250334634),
         (0.20153242868084004, 0.6903972848809445, 0.48555741928166823),
         (0.20198559307245323, 0.6897547200548507, 0.4949468757622348),
         (0.202424525380903, 0.6891300778516097, 0.503853671233272),
         (0.20285039084876416, 0.6885218992303662, 0.5123290742758754),
         (0.20326425554486904, 0.6879288396707249, 0.5204174105596941),
         (0.20366709796642735, 0.6873496561826712, 0.5281572829657327),
         (0.2040598191390614, 0.6867831958950266, 0.5355825350770153),
         (0.20444325144427355, 0.6862283859909593, 0.5427230209305143),
         (0.20481816636532163, 0.6856842247958556, 0.5496052265062291),
         (0.20518528131112984, 0.6851497738530601, 0.5562527763557912),
         (0.20554526565227554, 0.6846241508478893, 0.5626868502564876),
         (0.20589874608211323, 0.6841065232608877, 0.5689265286734352),
         (0.20624631139887467, 0.6835961026483528, 0.574989081375477),
         (0.2065885167903036, 0.6830921394623206, 0.5808902102817125),
         (0.20692588769061865, 0.6825939183339891, 0.5866442551784771),
         (0.2072589232698146, 0.682100753754371, 0.5922643691093119),
         (0.20758809960717012, 0.6816119860941408, 0.5977626688411679),
         (0.2079138725940713, 0.681126977911426, 0.6031503647343739),
         (0.20823668060563122, 0.6806451105019186, 0.6084378735097903),
         (0.20855694697590543, 0.6801657806503056, 0.613634916754686),
         (0.20887508230762786, 0.679688397545788, 0.6187506074957628),
         (0.20919148664422443, 0.6792123798274676, 0.6237935267612539),
         (0.20950655152921804, 0.6787371527277457, 0.6287717917301754),
         (0.20982066197609828, 0.678262145283619, 0.6336931168075463),
         (0.21013419837006558, 0.6777867875869759, 0.6385648687560636),
         (0.21044753832183283, 0.6773105080456748, 0.6433941168468681),
         (0.21076105849282406, 0.6768327306273811, 0.6481876788566628),
         (0.21107513641058356, 0.6763528720578337, 0.6529521636293766),
         (0.2113901522930482, 0.6758703389444077, 0.6576940108330298),
         (0.21170649090048915, 0.6753845247945096, 0.6624195284727574),
         (0.21202454343440974, 0.6748948068964544, 0.6671349286662659),
         (0.212344709503536, 0.6744005430279743, 0.6718463621461228),
         (0.2126673991782448, 0.6739010679543245, 0.6765599519226349),
         (0.21299303515636936, 0.6733956896739991, 0.6812818265204151),
         (0.21332205506540253, 0.6728836853652252, 0.6860181531903158),
         (0.21365491392867747, 0.6723642969805301, 0.6907751714956992),
         (0.21399208682626591, 0.6718367264295817, 0.6955592276779177),
         (0.21433407178514463, 0.6713001302819862, 0.7003768102204219),
         (0.2146813929378315, 0.6707536139114771, 0.7052345870546263),
         (0.21503460399425622, 0.6701962249906347, 0.7101394448841845),
         (0.21539429207828836, 0.6696269462304905, 0.7150985311488),
         (0.21576108198845112, 0.6690446872415565, 0.7201192992055431),
         (0.21613564095194687, 0.668448275371327, 0.725209557376853),
         (0.2165186839528287, 0.6678364453472654, 0.7303775226024408),
         (0.21691097972918683, 0.6672078275226823, 0.7356318795403709),
         (0.21731335755127784, 0.6665609344843629, 0.7409818460947873),
         (0.21772671491320644, 0.6658941457336356, 0.7464372465091529),
         (0.2181520262960297, 0.6652056900945817, 0.7520085933610736),
         (0.2185903531910598, 0.6644936254314854, 0.7577071800360629),
         (0.21904285561010112, 0.6637558151687588, 0.763545185553598),
         (0.21951080535638745, 0.6629899009957311, 0.7695357939831057),
         (0.21999560138816554, 0.6621932709996633, 0.7756933311376569),
         (0.22049878767967085, 0.6613630222949385, 0.7820334217918271),
         (0.22102207407544294, 0.6604959169937373, 0.7885731713670437),
         (0.2215673607491483, 0.6595883300790216, 0.7953313769016389),
         (0.2221367670243558, 0.6586361873746814, 0.8023287732251551),
         (0.22273266550170495, 0.6576348913334187, 0.8095883216556432),
         (0.22335772267769388, 0.6565792317435265, 0.8171355503265633),
         (0.22401494755251078, 0.6554632776400674, 0.8249989575508566),
         (0.22470775013240774, 0.6542802456224018, 0.8332104926136298),
         (0.2254400122700212, 0.6530223383270544, 0.8418061322860023),
         (0.2262161740011972, 0.6516805448369433, 0.8508265764975291),
         (0.22704133949704008, 0.6502443921137436, 0.8603180934531105),
         (0.2279214080519159, 0.6487016328087147, 0.8703335536880675),
         (0.22886323731317754, 0.6470378495747482, 0.8809337050681826),
         (0.22987484843441836, 0.6452359485654354, 0.8921887579440351),
         (0.23096568631232406, 0.6432755040816325, 0.9041803736151155),
         (0.23214695302050165, 0.6411319006107515, 0.917004183045936),
         (0.23343203971319598, 0.6387751950741376, 0.9307730111530477),
         (0.23483709278892512, 0.6361685864942893, 0.945621052367675),
         (0.24473932642858742, 0.6330306610304015, 0.9586903810237998),
         (0.2868712326700168, 0.6287105962211041, 0.9586664246292408),
         (0.3222663523784181, 0.6244158937009174, 0.9586428172331584),
         (0.3531380715309417, 0.6201408220829481, 0.9586195235634788),
         (0.38072246905632734, 0.6158797514728205, 0.9585965100225412),
         (0.4057924699282796, 0.6116271224807657, 0.9585737444803003),
         (0.42886947640320355, 0.6073774160006272, 0.9585511960843579),
         (0.450325009975823, 0.6031251233924865, 0.958528835084335),
         (0.4704350237747769, 0.5988647167123801, 0.9585066326683652),
         (0.489411303538076, 0.5945906186317321, 0.9584845608097387),
         (0.5074207611094126, 0.590297171680574, 0.9584625921219049),
         (0.5245978784733725, 0.5859786064320224, 0.958440699720207),
         (0.541053059252188, 0.5816290082201595, 0.9584188570888345),
         (0.5568784227218054, 0.5772422819484821, 0.9583970379515826),
         (0.5721519385333966, 0.5728121145000605, 0.9583752161450682),
         (0.5869404500664551, 0.5683319342017273, 0.9583533654930999),
         (0.6013019327874127, 0.5637948667205802, 0.9583314596809148),
         (0.615287213427127, 0.559193686678825, 0.9583094721280018),
         (0.6289413012168904, 0.5545207641584801, 0.9582873758581935),
         (0.6423044349219739, 0.5497680051256467, 0.9582651433656727),
         (0.6554129183639046, 0.5449267846282329, 0.9582427464754578),
         (0.6682997963586749, 0.5399878714026392, 0.9582201561968359),
         (0.6809954088258944, 0.534941342252636, 0.9581973425680851),
         (0.6935278509735336, 0.529776484222745, 0.9581742744906617),
         (0.7059233605053892, 0.5244816821591616, 0.9581509195508325),
         (0.7182066478139086, 0.5190442887074985, 0.9581272438264815),
         (0.7304011815064976, 0.5134504731029961, 0.9581032116765437),
         (0.7425294389660365, 0.5076850442173546, 0.9580787855101417),
         (0.7546131296930424, 0.5017312421709713, 0.9580539255320967),
         (0.766673397730214, 0.49557049130841185, 0.9580285894609609),
         (0.7787310083996071, 0.4891821053394407, 0.9580027322151125),
         (0.790806523797355, 0.4825429327842003, 0.95797630556172),
         (0.8029204709267095, 0.47562692726376427, 0.9579492577224819),
         (0.8150935059627381, 0.46840462225708906, 0.9579215329289891),
         (0.8273465779008055, 0.46084248312202275, 0.9578930709192442),
         (0.8397010947263905, 0.4529020995703274, 0.9578638063653008),
         (0.8521790952444983, 0.44453916803025, 0.9578336682200385),
         (0.8648034298189519, 0.43570219326558074, 0.9578025789687387),
         (0.877597953497515, 0.426330808746607, 0.9577704537681936),
         (0.8905877353470529, 0.41635356975626536, 0.9577371994524869),
         (0.9037992883094922, 0.40568500206085367, 0.9577027133800863),
         (0.9172608245380278, 0.3942215744230203, 0.9576668820912951),
         (0.9310025420172254, 0.3818360725321548, 0.9576295797380546),
         (0.9450569493561954, 0.3683695219250479, 0.9575906662391828),
         (0.9576373109362196, 0.35619136430478826, 0.9557359993354676),
         (0.9580946127058948, 0.36052898530935745, 0.9419662484998391),
         (0.9585268261197685, 0.364573629752603, 0.9286943394968231),
         (0.9589364383737439, 0.3683592173539925, 0.9158732840205942),
         (0.9593256315453976, 0.37191465435043286, 0.9034608724113244),
         (0.959696328706933, 0.3752647470590958, 0.8914190053817311),
         (0.9600502319591852, 0.3784309202380029, 0.8797131306598702),
         (0.9603888539940703, 0.3814317878772117, 0.8683117650835491),
         (0.9607135444377216, 0.38428361106607273, 0.8571860866654),
         (0.9610255119572891, 0.38700066848817355, 0.8463095842221552),
         (0.9613258429086012, 0.3895955586283379, 0.835657754551432),
         (0.9616155171433513, 0.3920794481113146, 0.8252078390086729),
         (0.9618954214714402, 0.39446227718346083, 0.8149385928073173),
         (0.9621663611779471, 0.3967529308286592, 0.8048300815272894),
         (0.9624290699185915, 0.3989593821259674, 0.7948635002383245),
         (0.9626842182576679, 0.40108881303409805, 0.785021011376729),
         (0.9629324210647748, 0.4031477167036946, 0.7752855980955682),
         (0.9631742439485064, 0.40514198458478756, 0.7656409302685112),
         (0.9634102088745581, 0.40707698095072226, 0.7560712406887493),
         (0.9636407990908468, 0.4089576069552029, 0.7465612092834406),
         (0.9638664634620825, 0.4107883559421659, 0.7370958533732269),
         (0.9640876202997261, 0.4125733614139001, 0.7276604221544372),
         (0.9643046607597797, 0.41431643881242525, 0.7182402936743032),
         (0.9645179518697552, 0.41602112206844516, 0.708820872610067),
         (0.9647278392369799, 0.4176906957105284, 0.6993874871516829),
         (0.9649346494828287, 0.4193282231962134, 0.6899252832229752),
         (0.9651386924411661, 0.4209365720202193, 0.6804191141525889),
         (0.9653402631540379, 0.42251843606792194, 0.6708534237157572),
         (0.9655396436933014, 0.4240763556108685, 0.6612121201984077),
         (0.9657371048332511, 0.4256127352823818, 0.6514784387689583),
         (0.9659329075962594, 0.4271298603228608, 0.6416347889557261),
         (0.9661273046909639, 0.42862991134431133, 0.6316625833853154),
         (0.9663205418604409, 0.430114977830506, 0.6215420430925309),
         (0.9665128591561202, 0.43158707056172113, 0.6112519735999935),
         (0.966704492151807, 0.4330481331303269, 0.6007695044938985),
         (0.9668956731110901, 0.43450005269484293, 0.5900697832615247),
         (0.9670866321205837, 0.43594467010477495, 0.5791256115201777),
         (0.9674139053806857, 0.43840763801794946, 0.5597212495317522),
         (0.9676054164533737, 0.4398414570582883, 0.5479529885633961)]

hsl = [(0.86, 0.3712, 0.33999999999999997),
       (0.86, 0.3833875, 0.33999999999999997),
       (0.86, 0.395575, 0.33999999999999997),
       (0.86, 0.40776249999999997, 0.33999999999999997),
       (0.86, 0.41995, 0.33999999999999997),
       (0.86, 0.43213749999999995, 0.33999999999999997),
       (0.86, 0.44432499999999997, 0.33999999999999997),
       (0.86, 0.4565125, 0.33999999999999997),
       (0.86, 0.4687, 0.33999999999999997),
       (0.86, 0.48088749999999997, 0.33999999999999997),
       (0.86, 0.493075, 0.33999999999999997),
       (0.86, 0.5052625, 0.33999999999999997),
       (0.86, 0.51745, 0.33999999999999997),
       (0.86, 0.5296375, 0.33999999999999997),
       (0.86, 0.541825, 0.33999999999999997),
       (0.86, 0.5540125, 0.33999999999999997),
       (0.86, 0.5661999999999999, 0.33999999999999997),
       (0.86, 0.5783874999999999, 0.33999999999999997),
       (0.86, 0.590575, 0.33999999999999997),
       (0.86, 0.6027625, 0.33999999999999997),
       (0.86, 0.6149499999999999, 0.33999999999999997),
       (0.86, 0.6271374999999999, 0.33999999999999997),
       (0.86, 0.6393249999999999, 0.33999999999999997),
       (0.86, 0.6515124999999999, 0.33999999999999997),
       (0.86, 0.6637, 0.33999999999999997),
       (0.86, 0.6758875, 0.33999999999999997),
       (0.86, 0.688075, 0.33999999999999997),
       (0.86, 0.7002625, 0.33999999999999997),
       (0.86, 0.71245, 0.33999999999999997),
       (0.86, 0.7246375, 0.33999999999999997),
       (0.86, 0.736825, 0.33999999999999997),
       (0.86, 0.7490125, 0.33999999999999997),
       (0.86, 0.7612000000000001, 0.33999999999999997),
       (0.86, 0.7733875, 0.33999999999999997),
       (0.86, 0.785575, 0.33999999999999997),
       (0.86, 0.7977625, 0.33999999999999997),
       (0.86, 0.80995, 0.33999999999999997),
       (0.86, 0.8221375, 0.33999999999999997),
       (0.86, 0.834325, 0.33999999999999997),
       (0.86, 0.8465125, 0.33999999999999997),
       (0.86, 0.8587, 0.33999999999999997),
       (0.8491125, 0.86, 0.33999999999999997),
       (0.8369250000000001, 0.86, 0.33999999999999997),
       (0.8247375, 0.86, 0.33999999999999997),
       (0.8125500000000001, 0.86, 0.33999999999999997),
       (0.8003625000000001, 0.86, 0.33999999999999997),
       (0.7881750000000001, 0.86, 0.33999999999999997),
       (0.7759875, 0.86, 0.33999999999999997),
       (0.7638, 0.86, 0.33999999999999997),
       (0.7516125000000001, 0.86, 0.33999999999999997),
       (0.7394250000000001, 0.86, 0.33999999999999997),
       (0.7272375, 0.86, 0.33999999999999997),
       (0.7150500000000001, 0.86, 0.33999999999999997),
       (0.7028625000000001, 0.86, 0.33999999999999997),
       (0.690675, 0.86, 0.33999999999999997),
       (0.6784875000000001, 0.86, 0.33999999999999997),
       (0.6663000000000001, 0.86, 0.33999999999999997),
       (0.6541125000000001, 0.86, 0.33999999999999997),
       (0.6419250000000001, 0.86, 0.33999999999999997),
       (0.6297375000000001, 0.86, 0.33999999999999997),
       (0.61755, 0.86, 0.33999999999999997),
       (0.6053625, 0.86, 0.33999999999999997),
       (0.593175, 0.86, 0.33999999999999997),
       (0.5809875000000001, 0.86, 0.33999999999999997),
       (0.5688000000000001, 0.86, 0.33999999999999997),
       (0.5566125000000001, 0.86, 0.33999999999999997),
       (0.544425, 0.86, 0.33999999999999997),
       (0.5322375000000001, 0.86, 0.33999999999999997),
       (0.5200500000000001, 0.86, 0.33999999999999997),
       (0.5078625000000001, 0.86, 0.33999999999999997),
       (0.4956750000000001, 0.86, 0.33999999999999997),
       (0.48348750000000007, 0.86, 0.33999999999999997),
       (0.47130000000000005, 0.86, 0.33999999999999997),
       (0.45911250000000003, 0.86, 0.33999999999999997),
       (0.44692500000000007, 0.86, 0.33999999999999997),
       (0.43473750000000005, 0.86, 0.33999999999999997),
       (0.4225500000000001, 0.86, 0.33999999999999997),
       (0.4103625000000001, 0.86, 0.33999999999999997),
       (0.39817500000000006, 0.86, 0.33999999999999997),
       (0.38598750000000004, 0.86, 0.33999999999999997),
       (0.3738000000000001, 0.86, 0.33999999999999997),
       (0.36161250000000006, 0.86, 0.33999999999999997),
       (0.34942500000000004, 0.86, 0.33999999999999997),
       (0.33999999999999997, 0.86, 0.3427625000000001),
       (0.33999999999999997, 0.86, 0.35495000000000004),
       (0.33999999999999997, 0.86, 0.36713750000000006),
       (0.33999999999999997, 0.86, 0.3793250000000001),
       (0.33999999999999997, 0.86, 0.39151250000000004),
       (0.33999999999999997, 0.86, 0.40370000000000006),
       (0.33999999999999997, 0.86, 0.4158875000000001),
       (0.33999999999999997, 0.86, 0.42807500000000004),
       (0.33999999999999997, 0.86, 0.44026250000000006),
       (0.33999999999999997, 0.86, 0.45245),
       (0.33999999999999997, 0.86, 0.46463750000000004),
       (0.33999999999999997, 0.86, 0.47682500000000005),
       (0.33999999999999997, 0.86, 0.48901250000000007),
       (0.33999999999999997, 0.86, 0.5012000000000001),
       (0.33999999999999997, 0.86, 0.5133875000000001),
       (0.33999999999999997, 0.86, 0.5255750000000001),
       (0.33999999999999997, 0.86, 0.5377625),
       (0.33999999999999997, 0.86, 0.54995),
       (0.33999999999999997, 0.86, 0.5621375000000001),
       (0.33999999999999997, 0.86, 0.5743250000000001),
       (0.33999999999999997, 0.86, 0.5865125),
       (0.33999999999999997, 0.86, 0.5987),
       (0.33999999999999997, 0.86, 0.6108875),
       (0.33999999999999997, 0.86, 0.623075),
       (0.33999999999999997, 0.86, 0.6352625000000001),
       (0.33999999999999997, 0.86, 0.6474500000000001),
       (0.33999999999999997, 0.86, 0.6596375000000001),
       (0.33999999999999997, 0.86, 0.6718250000000001),
       (0.33999999999999997, 0.86, 0.6840125),
       (0.33999999999999997, 0.86, 0.6962000000000002),
       (0.33999999999999997, 0.86, 0.7083875000000001),
       (0.33999999999999997, 0.86, 0.7205750000000001),
       (0.33999999999999997, 0.86, 0.7327625000000001),
       (0.33999999999999997, 0.86, 0.7449500000000001),
       (0.33999999999999997, 0.86, 0.7571375),
       (0.33999999999999997, 0.86, 0.769325),
       (0.33999999999999997, 0.86, 0.7815125),
       (0.33999999999999997, 0.86, 0.7937000000000001),
       (0.33999999999999997, 0.86, 0.8058875000000001),
       (0.33999999999999997, 0.86, 0.8180750000000001),
       (0.33999999999999997, 0.86, 0.8302625000000001),
       (0.33999999999999997, 0.86, 0.84245),
       (0.33999999999999997, 0.86, 0.8546375),
       (0.33999999999999997, 0.8531749999999998, 0.86),
       (0.33999999999999997, 0.8409874999999999, 0.86),
       (0.33999999999999997, 0.8287999999999999, 0.86),
       (0.33999999999999997, 0.8166124999999999, 0.86),
       (0.33999999999999997, 0.8044249999999998, 0.86),
       (0.33999999999999997, 0.7922374999999999, 0.86),
       (0.33999999999999997, 0.7800499999999999, 0.86),
       (0.33999999999999997, 0.7678624999999998, 0.86),
       (0.33999999999999997, 0.7556749999999999, 0.86),
       (0.33999999999999997, 0.7434874999999999, 0.86),
       (0.33999999999999997, 0.7312999999999998, 0.86),
       (0.33999999999999997, 0.7191124999999998, 0.86),
       (0.33999999999999997, 0.7069249999999998, 0.86),
       (0.33999999999999997, 0.6947374999999998, 0.86),
       (0.33999999999999997, 0.6825499999999998, 0.86),
       (0.33999999999999997, 0.6703624999999999, 0.86),
       (0.33999999999999997, 0.6581749999999998, 0.86),
       (0.33999999999999997, 0.6459874999999998, 0.86),
       (0.33999999999999997, 0.6337999999999998, 0.86),
       (0.33999999999999997, 0.6216124999999999, 0.86),
       (0.33999999999999997, 0.6094249999999999, 0.86),
       (0.33999999999999997, 0.5972374999999999, 0.86),
       (0.33999999999999997, 0.5850499999999998, 0.86),
       (0.33999999999999997, 0.5728624999999998, 0.86),
       (0.33999999999999997, 0.5606749999999998, 0.86),
       (0.33999999999999997, 0.5484874999999998, 0.86),
       (0.33999999999999997, 0.5362999999999998, 0.86),
       (0.33999999999999997, 0.5241124999999999, 0.86),
       (0.33999999999999997, 0.5119249999999999, 0.86),
       (0.33999999999999997, 0.49973749999999983, 0.86),
       (0.33999999999999997, 0.4875499999999998, 0.86),
       (0.33999999999999997, 0.47536249999999985, 0.86),
       (0.33999999999999997, 0.46317499999999984, 0.86),
       (0.33999999999999997, 0.4509874999999999, 0.86),
       (0.33999999999999997, 0.43879999999999986, 0.86),
       (0.33999999999999997, 0.42661249999999984, 0.86),
       (0.33999999999999997, 0.4144249999999998, 0.86),
       (0.33999999999999997, 0.4022374999999998, 0.86),
       (0.33999999999999997, 0.39004999999999984, 0.86),
       (0.33999999999999997, 0.3778624999999998, 0.86),
       (0.33999999999999997, 0.3656749999999998, 0.86),
       (0.33999999999999997, 0.35348749999999984, 0.86),
       (0.33999999999999997, 0.3412999999999998, 0.86),
       (0.35088749999999974, 0.33999999999999997, 0.86),
       (0.36307499999999976, 0.33999999999999997, 0.86),
       (0.3752624999999998, 0.33999999999999997, 0.86),
       (0.38744999999999974, 0.33999999999999997, 0.86),
       (0.39963749999999976, 0.33999999999999997, 0.86),
       (0.4118249999999998, 0.33999999999999997, 0.86),
       (0.4240124999999998, 0.33999999999999997, 0.86),
       (0.43619999999999975, 0.33999999999999997, 0.86),
       (0.4483874999999998, 0.33999999999999997, 0.86),
       (0.46057499999999973, 0.33999999999999997, 0.86),
       (0.47276249999999975, 0.33999999999999997, 0.86),
       (0.48494999999999977, 0.33999999999999997, 0.86),
       (0.4971374999999998, 0.33999999999999997, 0.86),
       (0.5093249999999998, 0.33999999999999997, 0.86),
       (0.5215124999999998, 0.33999999999999997, 0.86),
       (0.5336999999999998, 0.33999999999999997, 0.86),
       (0.5458874999999997, 0.33999999999999997, 0.86),
       (0.5580749999999998, 0.33999999999999997, 0.86),
       (0.5702624999999998, 0.33999999999999997, 0.86),
       (0.5824499999999998, 0.33999999999999997, 0.86),
       (0.5946374999999997, 0.33999999999999997, 0.86),
       (0.6068249999999997, 0.33999999999999997, 0.86),
       (0.6190124999999997, 0.33999999999999997, 0.86),
       (0.6311999999999998, 0.33999999999999997, 0.86),
       (0.6433874999999998, 0.33999999999999997, 0.86),
       (0.6555749999999998, 0.33999999999999997, 0.86),
       (0.6677624999999998, 0.33999999999999997, 0.86),
       (0.6799499999999998, 0.33999999999999997, 0.86),
       (0.6921374999999999, 0.33999999999999997, 0.86),
       (0.7043249999999998, 0.33999999999999997, 0.86),
       (0.7165124999999998, 0.33999999999999997, 0.86),
       (0.7286999999999998, 0.33999999999999997, 0.86),
       (0.7408874999999998, 0.33999999999999997, 0.86),
       (0.7530749999999997, 0.33999999999999997, 0.86),
       (0.7652624999999997, 0.33999999999999997, 0.86),
       (0.7774499999999998, 0.33999999999999997, 0.86),
       (0.7896374999999998, 0.33999999999999997, 0.86),
       (0.8018249999999998, 0.33999999999999997, 0.86),
       (0.8140124999999998, 0.33999999999999997, 0.86),
       (0.8261999999999998, 0.33999999999999997, 0.86),
       (0.8383874999999998, 0.33999999999999997, 0.86),
       (0.8505749999999997, 0.33999999999999997, 0.86),
       (0.86, 0.33999999999999997, 0.8572374999999997),
       (0.86, 0.33999999999999997, 0.8450499999999996),
       (0.86, 0.33999999999999997, 0.8328624999999996),
       (0.86, 0.33999999999999997, 0.8206749999999996),
       (0.86, 0.33999999999999997, 0.8084874999999996),
       (0.86, 0.33999999999999997, 0.7962999999999996),
       (0.86, 0.33999999999999997, 0.7841124999999995),
       (0.86, 0.33999999999999997, 0.7719249999999996),
       (0.86, 0.33999999999999997, 0.7597374999999996),
       (0.86, 0.33999999999999997, 0.7475499999999996),
       (0.86, 0.33999999999999997, 0.7353624999999997),
       (0.86, 0.33999999999999997, 0.7231749999999996),
       (0.86, 0.33999999999999997, 0.7109874999999997),
       (0.86, 0.33999999999999997, 0.6987999999999996),
       (0.86, 0.33999999999999997, 0.6866124999999996),
       (0.86, 0.33999999999999997, 0.6744249999999996),
       (0.86, 0.33999999999999997, 0.6622374999999996),
       (0.86, 0.33999999999999997, 0.6500499999999996),
       (0.86, 0.33999999999999997, 0.6378624999999996),
       (0.86, 0.33999999999999997, 0.6256749999999995),
       (0.86, 0.33999999999999997, 0.6134874999999996),
       (0.86, 0.33999999999999997, 0.6012999999999996),
       (0.86, 0.33999999999999997, 0.5891124999999996),
       (0.86, 0.33999999999999997, 0.5769249999999996),
       (0.86, 0.33999999999999997, 0.5647374999999997),
       (0.86, 0.33999999999999997, 0.5525499999999997),
       (0.86, 0.33999999999999997, 0.5403624999999996),
       (0.86, 0.33999999999999997, 0.5281749999999996),
       (0.86, 0.33999999999999997, 0.5159874999999996),
       (0.86, 0.33999999999999997, 0.5037999999999996),
       (0.86, 0.33999999999999997, 0.49161249999999956),
       (0.86, 0.33999999999999997, 0.4794249999999996),
       (0.86, 0.33999999999999997, 0.4672374999999996),
       (0.86, 0.33999999999999997, 0.4550499999999996),
       (0.86, 0.33999999999999997, 0.4428624999999996),
       (0.86, 0.33999999999999997, 0.4306749999999996),
       (0.86, 0.33999999999999997, 0.41848749999999957),
       (0.86, 0.33999999999999997, 0.4062999999999996),
       (0.86, 0.33999999999999997, 0.3941124999999996),
       (0.86, 0.33999999999999997, 0.3819249999999996),
       (0.86, 0.33999999999999997, 0.3697374999999996),
       (0.86, 0.33999999999999997, 0.3575499999999996),
       (0.86, 0.33999999999999997, 0.3453624999999996),
       (0.86, 0.346825, 0.33999999999999997),
       (0.86, 0.3590125, 0.33999999999999997)]


hsluv_cmap = ListedColormap(hsluv)

hsl_cmap = ListedColormap(hsl)