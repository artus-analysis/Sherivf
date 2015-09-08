#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

void VP2_4_16_10_434_64_18_2::SetCouplFlav(vector<Complex>& coupl)
{
  f[0] = 23;
  f[1] = 22;
  f[2] = 21;
  f[3] = 1;

  for (int i=0;i<10;i++) c[i] = coupl[i];
  for (int i=0;i<64;i++)
    for (int j=0;j<8;j++) M[i][j] = Complex(0.,0.);

  Z[0] = Complex(0.,0.);
}

void VP2_4_16_10_434_64_18_2::Calculate()
{
  for(int i=0;i<64;i++) cl[i] = 0;

  Calculate_1();
  Calculate_2();
}
