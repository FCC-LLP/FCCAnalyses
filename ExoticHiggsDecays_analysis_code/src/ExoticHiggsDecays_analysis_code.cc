// -*- C++ -*-
//
/** FCCAnalysis module: ExoticHiggsDecays_analysis_code
 *
 * \file ExoticHiggsDecays_analysis_code.cc
 * \author <mvoorde> <<m.voorde96@gmail.com>>
 */

#include "ExoticHiggsDecays_analysis_code.h"
#include <iostream>

using namespace std;

namespace ExoticHiggsDecays_analysis_code {
  void dummy_analysis() { cout << "Dummy analysis initialised." << endl; }

  rv::RVec<float> dummy_collection(const rv::RVec<edm4hep::ReconstructedParticleData>& parts) {
    rv::RVec<float> output;
    for (size_t i = 0; i < parts.size(); ++i)
      output.emplace_back(parts.at(i).momentum.x);
    return output;
  }

  ROOT::VecOps::RVec<float> get_both_scalars(ROOT::VecOps::RVec<float> scalar1_value, ROOT::VecOps::RVec<float> scalar2_value) {
  ROOT::VecOps::RVec<float> sum;
  for (auto i: scalar1_value) {
    sum.push_back(i);
  }
  for (auto j: scalar2_value) {
    sum.push_back(j);
  }
  return sum;
}

// following code is copied from https://github.com/HEP-FCC/FCCAnalyses/blob/09c52e107e308cf57d59ca840d4bba60e25d94c2/examples/FCCee/flavour/Bc2TauNu/analysis_B2TauNu_truth.py 
// used to find the b quarks from respective hs. Can't directly apply sel_byIndex since this function returns a 'edm4hep::MCParticleData' object and we need 'ROOT::VecOps::RVec<edm4hep::MCParticleData>'

selMC_leg::selMC_leg( int arg_idx ) : m_idx(arg_idx) { };
ROOT::VecOps::RVec<edm4hep::MCParticleData> selMC_leg::operator() ( ROOT::VecOps::RVec<int> list_of_indices,  ROOT::VecOps::RVec<edm4hep::MCParticleData> in) {
  ROOT::VecOps::RVec<edm4hep::MCParticleData> res;
  if ( list_of_indices.size() == 0) return res;
  if ( m_idx < list_of_indices.size() ) {
	res.push_back( FCCAnalyses::MCParticle::sel_byIndex( list_of_indices[m_idx], in ) );
	return res;
  }
  else {
	std::cout << "   !!!  in selMC_leg:  idx = " << m_idx << " but size of list_of_indices = " << list_of_indices.size() << std::endl;
  }
  return res;
}
}  // end namespace ExoticHiggsDecays_analysis_code
