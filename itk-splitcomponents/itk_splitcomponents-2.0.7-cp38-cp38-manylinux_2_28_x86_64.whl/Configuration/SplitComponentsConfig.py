depends = ('ITKPyBase', 'ITKCommon', )
templates = (  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterIVF22IF2', True, 'itk::Image< itk::Vector< float,2 >,2 >, itk::Image< float,2 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterIVF33IF3', True, 'itk::Image< itk::Vector< float,3 >,3 >, itk::Image< float,3 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterIVF44IF4', True, 'itk::Image< itk::Vector< float,4 >,4 >, itk::Image< float,4 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterICVF22IF2', True, 'itk::Image<itk::CovariantVector<float, 2>, 2>, itk::Image< float,2 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterICVF33IF3', True, 'itk::Image<itk::CovariantVector<float, 3>, 3>, itk::Image< float,3 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterICVF44IF4', True, 'itk::Image<itk::CovariantVector<float, 4>, 4>, itk::Image< float,4 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterVISS2ISS2', True, 'itk::VectorImage< signed short,2 >,itk::Image< signed short,2 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterVIUC2IUC2', True, 'itk::VectorImage< unsigned char,2 >,itk::Image< unsigned char,2 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterVIUS2IUS2', True, 'itk::VectorImage< unsigned short,2 >,itk::Image< unsigned short,2 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterVIF2IF2', True, 'itk::VectorImage< float,2 >,itk::Image< float,2 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterVID2ID2', True, 'itk::VectorImage< double,2 >,itk::Image< double,2 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterVISS3ISS3', True, 'itk::VectorImage< signed short,3 >,itk::Image< signed short,3 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterVIUC3IUC3', True, 'itk::VectorImage< unsigned char,3 >,itk::Image< unsigned char,3 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterVIUS3IUS3', True, 'itk::VectorImage< unsigned short,3 >,itk::Image< unsigned short,3 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterVIF3IF3', True, 'itk::VectorImage< float,3 >,itk::Image< float,3 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterVID3ID3', True, 'itk::VectorImage< double,3 >,itk::Image< double,3 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterVISS4ISS4', True, 'itk::VectorImage< signed short,4 >,itk::Image< signed short,4 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterVIUC4IUC4', True, 'itk::VectorImage< unsigned char,4 >,itk::Image< unsigned char,4 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterVIUS4IUS4', True, 'itk::VectorImage< unsigned short,4 >,itk::Image< unsigned short,4 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterVIF4IF4', True, 'itk::VectorImage< float,4 >,itk::Image< float,4 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterVID4ID4', True, 'itk::VectorImage< double,4 >,itk::Image< double,4 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterIRGBUC2IUC2', True, 'itk::Image< itk::RGBPixel< unsigned char >,2 >, itk::Image< unsigned char,2 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterIRGBUC3IUC3', True, 'itk::Image< itk::RGBPixel< unsigned char >,3 >, itk::Image< unsigned char,3 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterIRGBUC4IUC4', True, 'itk::Image< itk::RGBPixel< unsigned char >,4 >, itk::Image< unsigned char,4 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterIRGBAUC2IUC2', True, 'itk::Image< itk::RGBAPixel< unsigned char >,2 >, itk::Image< unsigned char,2 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterIRGBAUC3IUC3', True, 'itk::Image< itk::RGBAPixel< unsigned char >,3 >, itk::Image< unsigned char,3 >'),
  ('SplitComponentsImageFilter', 'itk::SplitComponentsImageFilter', 'itkSplitComponentsImageFilterIRGBAUC4IUC4', True, 'itk::Image< itk::RGBAPixel< unsigned char >,4 >, itk::Image< unsigned char,4 >'),
)
factories = ()
