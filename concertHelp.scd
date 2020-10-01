
t = Konsert();
s.options.device = "UltraLite-mk4"; //FIRST STEP
s.meter;s.plotTree;
(
~gatorsettings = (inBusA:t.aBus, inBusB:t.bBus, outBus:t.panBusC, revOut: t.revBus, lag:10, clampT:0.1, relT:1, gate:1, thresh:0.5);
t.gator(~gatorsettings);
)

(
~moog = Synth(\moog, [\inBus, 1, \outBus, t.aBus, \amp, 1], t.synthGroup);
~korg = Synth(\D1200, [\inBus, 2, \outBus, t.bBus], t.synthGroup);
~mic = Synth(\mic, [\inBus, 0, \outBus, t.outBus], t.synthGroup);

~gatorsettings = (inBusA:t.aBus, inBusB:t.bBus, outBus:t.panBusC, revOut: t.revBus, lag:10, clampT:0.01, relT:0.5, gate:1);
t.gator(~gatorsettings);
~passGator = Synth(\noGator, [\inBus, t.outBus, \outBus, t.panBusD, \revOut, t.revBus], t.fxGroup, 'addToHead');
~reverb = Synth(\reverb, [\inBus, t.revBus, \outBus, t.panBusD], t.fxGroup, 'addToTail'); //t.panBus or t.panBusD

~pannerCircle = Synth(\pannerCircle, [\inBus,  t.panBusC, \outBus, 2, \speed, 0.1, \level, 1, \dir, 1], t.panGroup, 'addToTail');
~out = Synth(\outSynth, [\inBus, t.panBus, \outBus, 2,\outBus1, 4], t.panGroup);
)


//////////////////////TUNING
///////////////////////
///////////////////////
(
~sine = {Out.ar(2, SinOsc.ar(440)*0.04)}.play;
Pbindef(\midiTuning,
	\type, \midi,
	\midicmd, \noteOn,
	\midiout, t.midiBus,
	\chan, 0,
	\midinote, 69,
	\dur, Pseq([3], inf),
).play;
~moog0 = Synth(\moog, [\inBus, 1, \outBus, 3, \amp, 1]);
)
Pbindef(\midiTuning).stop;
~sine.free;
~moog0.free;
~moog0.set(\inBus, 1, \outBus, 1, \amp, 1);

/////////////////////// STOP
///////////////////////
///////////////////////
(
~konsert.next;
~korg.free;
~moog.free;
~mic.free;
~grainSynth.free;
Pbindef(\midiMoog).stop;
Pbindef(\midiMoog1).stop;
Pbindef(\midiMoog2).stop;
Pbindef(\midiMoog3).stop;
Pbindef(\midiMoog4).stop;
Pbindef(\klank).stop;
Pbindef(\brownPan).stop;
Pbindef(\brownPan0).stop;
Pbindef(\panning).stop;
)

