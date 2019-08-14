from pycleanlens import cleanlens

model = cleanlens()
model.read_cleanset('a521.par')
model.imframe = '../../HST/A521_F606w_cut_ext1.fits'
model.sframe = 'TEST_pycleanset.fits'
model.print_param()

model.draw_dwcs_region(output='test.dwcs',update=True)
