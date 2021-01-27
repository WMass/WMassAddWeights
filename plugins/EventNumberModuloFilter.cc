// -*- C++ -*-
//
// Package:    EventNumberModuloFilter
// Class:      EventNumberModuloFilter
//
/**\class EventNumberModuloFilter EventNumberModuloFilter.cc filter/EventNumberModuloFilter/src/EventNumberModuloFilter.cc

Description: 

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Martin Grunewald
//         Created:  Tue Jan 22 13:55:00 CET 2008
//
//

// system include files
#include <string>
#include <iostream>
#include <memory>

// user include files
#include "EventNumberModuloFilter.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"

//
// constructors and destructor
//
EventNumberModuloFilter::EventNumberModuloFilter(const edm::ParameterSet& iConfig) {
  //now do what ever initialization is needed

  period_ = iConfig.getParameter<unsigned int>("period");
  remainder_ = iConfig.getParameter<unsigned int>("remainder");
  invert_ = iConfig.getParameter<bool>("invert");
}

EventNumberModuloFilter::~EventNumberModuloFilter() {
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
}

void EventNumberModuloFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<uint>("period", 5);
  desc.add<uint>("remainder", 0);
  desc.add<bool>("invert", false);
  descriptions.add("EventNumberModuloFilter", desc);
}

//
// member functions
//

// ------------ method called on each new Event  ------------
bool EventNumberModuloFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  bool accept(false);
  if (period_ != 0)
    accept = (((iEvent.id().event()) % period_) == remainder_);
  if (invert_)
    accept = !accept;
  return accept;
}

// declare this class as a framework plugin
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventNumberModuloFilter);
