var myApp = angular.module('myApp', ['ngMessages', 'ngResource']);

myApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  });


myApp.controller('mainController', ['$scope', '$resource', '$timeout', '$filter', '$http',
function($scope, $resource, $timeout, $filter, $http) {

	
	$scope.handle = '';

	$timeout(function() {

		$scope.name = 'Vedder';
	}, 3000);

	$scope.lowercasehandle = function() {
		return $filter('lowercase')($scope.handle);
	};

	$scope.characters = 5;

	// $scope.rules = [

	// 	{ rulename: "Must be 5 characters"},
	// 	{ rulename: "Must be original"},
	// 	{ rulename: "Must be cool"}

	// ];


	$http.get('http://127.0.0.1:8000/api/projects/chat/28')
		.success(function (result) {

			$scope.chat = result;

		})

		.error(function (data, status) {

			console.log(data);

		})




}]);